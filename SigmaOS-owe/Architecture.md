# Architecture — SigmaOS-owe

Extracted from the repository README.

## Performance design

- A still background does not keep the renderer. `owed` enables the shell
  background plugin, parks `owe-render` 2 seconds later, and stops it after
  1 more minute. Then only the 4 MiB daemon runs. During the switch, the
  video holds its current frame. A video or GIF starts the renderer again.
- Video renders only when `libmpv` signals a new frame. The render rate
  tracks the media frame rate, not the display refresh rate. A fade draws
  on each frame callback until it ends. A still that stays on screen does
  not commit again.
- A looping video plays as a list of copies of the file (an mpv EDL), so
  its last frame runs into its first like any other frame. mpv's own file
  loop holds the last frame about one frame too long and then cuts the
  first one short. The file is opened once for all copies, and the
  reported position stays within one copy. Only MP4/MOV and Matroska/WebM
  files without audio, whose timestamps start at 0 and whose length is
  known, play this way; other files loop on their own as before.
- A switch from a still to a video crossfades. The renderer draws the
  outgoing still over the incoming video and fades it out.
- Video draws straight into the window framebuffer. No intermediate
  copy per frame per output.
- Video redraws wait for the compositor's frame callback. A blanked
  output stops the draw loop instead of stalling the event loop, and an
  output covered by a fullscreen window stops swapping buffers.
- A commit marks the surface opaque when the frame has no transparent
  pixel. This covers video frames, and a still with no transparent pixel
  after its fade. The compositor can then skip what is below the wallpaper
  and draw it without blending. While a still fades in, the surface has no
  opaque region, so the compositor blends it. A crossfade over video keeps
  the opaque region, because the video below it keeps the alpha at 1.
- Hardware decode is on by default. When OpenGL renders on Intel or AMD,
  the renderer decodes with `vaapi,vaapi-copy` and ignores
  `LIBVA_DRIVER_NAME=nvidia`, so a hybrid laptop decodes on the GPU that
  renders. Nouveau decodes in software, because its video decoder needs
  firmware that `linux-firmware` does not ship. Other GPUs use
  `hwdec=auto-safe`. Override the decoder with the `OWE_HWDEC` environment
  variable.
- The renderer uses desktop OpenGL 3.2 or later. If the driver has no
  such context, as on some ARM SoCs, the renderer uses OpenGL ES 3.0 or later.
- `libmpv` runs without its lua scripts. The ytdl hook, stats overlay,
  console, and the other scripts only add threads and memory. Advanced
  mpv tuning uses `OWE_MPV_OPTIONS`, a semicolon separated list such as
  `demuxer-max-bytes=16MiB;hwdec-extra-frames=1`.
- Video larger than the output is shrunk with mpv's `hermite` filter and
  `correct-downscaling`, so thin lines match the same picture as a still
  instead of the harsher look of plain bilinear sampling.
- Stills decode once at the size the cover crop needs, upload one texture,
  and then stop the frame loop. Paused video stops the loop too.
- Layer surfaces use `wp_fractional_scale_v1` and `wp_viewporter` when the
  compositor offers them. A 1.25 scale output draws 1.25x pixels, not the 2x
  that `wl_output.scale` alone would ask for. Without the protocols the
  renderer falls back to the integer `wl_output.scale`.
- Stills and video cover the output. Aspect ratio is preserved with a
  center crop, like `PreserveAspectCrop` in the SigmaOS shell.
- The renderer returns freed large allocations to the OS. glibc keeps
  them resident by default, which inflates RSS by about 30 MiB with
  media buffers.
- Poster extraction and GIF transcode run in a worker thread. The
  daemon event loop never blocks on `ffmpeg`.
- The daemon sends pause and resume only when playback state changes.
