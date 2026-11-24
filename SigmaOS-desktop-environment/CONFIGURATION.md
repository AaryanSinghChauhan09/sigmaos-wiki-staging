# Desktop Environment Configuration

## Session Configuration

### Wayland Session

```bash
# /etc/sigmaos/session.conf
[session]
type=wayland
compositor=hyprland
display_server=wayland
shell=ags
launcher=walker
```

### X11 Session

```bash
# /etc/sigmaos/session.conf
[session]
type=x11
window_manager=openbox
display_server=x11
shell=polybar
launcher=rofi
```

## Window Manager Configuration

### Hyprland Configuration

```bash
# ~/.config/hypr/hyprland.conf
monitor=,preferred,auto,1
env=QT_QPA_PLATFORM,wayland
env=XDG_SESSION_TYPE,wayland
exec-once=ags shell
exec-once=walker --gapplication-service

# Input
input {
    kb_layout = us
    follow_mouse = 1
    sensitivity = 0
}

# General
general {
    gaps_in = 5
    gaps_out = 10
    border_size = 2
    col.active_border = rgba(33ccffee) rgba(00ff99ee) 45deg
    col.inactive_border = rgba(595959aa)
}

# Animations
animations {
    enabled = true
    bezier = myBezier, 0.05, 0.9, 0.1, 1.05
    animation = windows, 1, 7, myBezier, popin 80%
    animation = windowsOut, 1, 4, myBezier, popin 80%
    animation = fade, 1, 6, default, fade
    animation = workspaces, 1, 6, myBezier, slide
}

# Keybindings
general {
    bind = SUPER, Q, exec, kitty
    bind = SUPER, D, exec, walker --gapplication-service
    bind = SUPER, RETURN, exec, kitty
    bind = SUPER SHIFT, E, exec, thunar
    bind = SUPER SHIFT, Q, killactive
    bind = SUPER SHIFT, SPACE, exec, wofi --show drun
    bind = SUPER ALT, LEFT, movewindow, l
    bind = SUPER ALT, RIGHT, movewindow, r
    bind = SUPER ALT, UP, movewindow, u
    bind = SUPER ALT, DOWN, movewindow, d
    bind = SUPER SHIFT ALT, LEFT, resizeactive, -50 0
    bind = SUPER SHIFT ALT, RIGHT, resizeactive, 50 0
    bind = SUPER SHIFT ALT, UP, resizeactive, 0 -50
    bind = SUPER SHIFT ALT, DOWN, resizeactive, 0 50
    bind = SUPER, TAB, cyclenext
    bind = SUPER SHIFT, TAB, cyclenext, previous
    bind = SUPER, 1, workspace, 1
    bind = SUPER, 2, workspace, 2
    bind = SUPER, 3, workspace, 3
    bind = SUPER, 4, workspace, 4
    bind = SUPER, 5, workspace, 5
    bind = SUPER, 6, workspace, 6
    bind = SUPER, 7, workspace, 7
    bind = SUPER, 8, workspace, 8
    bind = SUPER, 9, workspace, 9
    bind = SUPER SHIFT, 1, movetoworkspace, 1
    bind = SUPER SHIFT, 2, movetoworkspace, 2
    bind = SUPER SHIFT, 3, movetoworkspace, 3
    bind = SUPER SHIFT, 4, movetoworkspace, 4
    bind = SUPER SHIFT, 5, movetoworkspace, 5
    bind = SUPER SHIFT, 6, movetoworkspace, 6
    bind = SUPER SHIFT, 7, movetoworkspace, 7
    bind = SUPER SHIFT, 8, movetoworkspace, 8
    bind = SUPER SHIFT, 9, movetoworkspace, 9
}
```

## Display Configuration

### Monitor Configuration

```bash
# ~/.config/hypr/monitors.conf
monitor=,preferred,auto,1
monitor=DP-1,2560x1440@144,0x0,1
monitor=HDMI-A-1,1920x1080@60,2560x0,1
```

### Display Settings

```bash
# /etc/sigmaos/display.conf
[display]
default_resolution=1920x1080
default_refresh_rate=60
scaling=1.0
night_light=false
color_profile=sRGB
multi_monitor=true
taskbar=all
wallpaper=per-monitor
```

## Theming Configuration

### Theme Configuration

```bash
# ~/.config/sigmaos/theme.conf
[theme]
name=sigmaos-dark
accent_color=#007bff
bg_primary=#1a1a1a
bg_secondary=#2d2d2d
bg_tertiary=#404040
text_primary=#ffffff
text_secondary=#b3b3b3
text_tertiary=#808080
border_primary=#404040
border_secondary=#505050
font_family=Inter
font_size=12
icon_theme=Papirus-Dark
cursor_theme=Bibata-Modern-Amber
wallpaper=/usr/share/sigmaos/wallpapers/default.jpg
transparency=0.8
animations=true
animation_speed=normal
```

### Custom Theme

```css
/* ~/.config/sigmaos/themes/custom.css */
:root {
  --color-primary: #007bff;
  --color-accent: #ff6b6b;
  --bg-primary: #1a1a1a;
  --bg-secondary: #2d2d2d;
  --text-primary: #ffffff;
  --text-secondary: #b3b3b3;
  --border-primary: #404040;
  --font-family: 'Inter', sans-serif;
  --font-size: 12px;
}
```

## Widget Configuration

### Widget Settings

```bash
# ~/.config/sigmaos/widgets.conf
[widgets]
clock={
  position="top-right",
  format="%H:%M:%S",
  show_date=true,
  show_seconds=true
}
weather={
  position="top-left",
  location="auto",
  units="metric",
  show_forecast=true
}
system_monitor={
  position="top-right",
  show_cpu=true,
  show_memory=true,
  show_disk=true,
  show_network=true
}
battery={
  position="top-right",
  show_percentage=true,
  show_time_remaining=true
}
```

## Notification Configuration

### Notification Settings

```bash
# ~/.config/sigmaos/notifications.conf
[notifications]
dnd=false
dnd_schedule=22:00-08:00
sound=true
sound_volume=50
preview=true
history=true
history_limit=100
actions=true
vibration=false
focus_mode=false
```

### Notification Rules

```bash
# ~/.config/sigmaos/notification-rules.conf
[applications]
firefox={
  dnd=true,
  sound=false,
  preview=false
}
slack={
  dnd=true,
  sound=false,
  preview=true
}
email={
  dnd=false,
  sound=true,
  preview=true
}
system={
  dnd=false,
  sound=true,
  preview=true
}
```

## Accessibility Configuration

### Accessibility Settings

```bash
# ~/.config/sigmaos/accessibility.conf
[accessibility]
screen_reader=false
high_contrast=false
large_text=false
text_scale=1.0
reduce_motion=false
focus_indicators=true
keyboard_navigation=true
sticky_keys=false
slow_keys=false
bounce_keys=false
mouse_keys=false
dwell_clicking=false
eye_tracking=false
switch_access=false
voice_control=false
visual_alerts=false
closed_captions=false
sound_amplification=false
audio_description=false
hearing_aid=false
mono_audio=false
audio_balance=0.5
equalizer=false
```

## Performance Configuration

### Performance Settings

```bash
# ~/.config/sigmaos/performance.conf
[performance]
gpu_acceleration=true
compositing=true
memory_management=balanced
cpu_optimization=performance
io_optimization=balanced
startup_time=fast
resource_usage=low
battery_life=optimized
animations=true
animation_speed=normal
transparency=0.8
blur=true
shadows=true
```

## Troubleshooting

### Common Issues

**Display issues:**
```bash
# Check display configuration
sigmaos-desktop display info

# Reset display settings
sigmaos-desktop display reset

# Switch display server
sigmaos-desktop session switch --type x11
```

**Window manager issues:**
```bash
# Restart window manager
sigmaos-desktop wm restart

# Reset window manager config
sigmaos-desktop wm reset

# Check window manager logs
sigmaos-desktop wm logs
```

**Performance issues:**
```bash
# Check system resources
sigmaos-desktop system resources

# Reduce animations
sigmaos-desktop effects reduce

# Disable transparency
sigmaos-desktop effects transparency off
```

## Best Practices

### Configuration Management

- Use version control for configuration files
- Backup configurations regularly
- Document custom configurations
- Test configurations in VM first
- Use configuration templates
- Keep configurations organized
- Use environment variables for sensitive data

### Performance Optimization

- Disable unused widgets
- Reduce animation complexity
- Optimize wallpaper resolution
- Use hardware acceleration
- Monitor resource usage
- Profile performance regularly
- Optimize for your hardware

### Security

- Keep system updated
- Use secure authentication
- Enable firewall
- Use encrypted storage
- Backup important data
- Monitor security logs
- Follow security best practices
