# SigmaOS Desktop Environment

## Overview

SigmaOS Desktop Environment provides a modern, cohesive desktop experience with window management, application launching, system settings, and user customization. It integrates seamlessly with SigmaOS core system components and provides a polished user interface.

## Key Features

- **Modern UI** - Clean, modern desktop interface with consistent design
- **Window Management** - Advanced window management with tiling and floating support
- **Application Launcher** - Fast application launcher with search and categories
- **System Settings** - Comprehensive system settings and preferences
- **Theming** - Customizable themes and visual styles
- **Widgets** - Desktop widgets for system information and productivity
- **Notifications** - Rich notification system with actions and history
- **Multi-Monitor** - Multi-monitor support with per-monitor settings
- **Accessibility** - Accessibility features for users with disabilities
- **Performance** - Optimized for performance and low resource usage

## Components

- **Window Manager** - Tiling and floating window management
- **Compositor** - Hardware-accelerated compositing and effects
- **Display Server** - Wayland/X11 display server integration
- **Shell** - Desktop shell with panels, menus, and widgets
- **Launcher** - Application launcher with fuzzy search
- **Settings** - System settings and preferences
- **Notifications** - Notification daemon and UI
- **Theming** - Theme engine and customization
- **Widgets** - Desktop widget framework
- **Accessibility** - Accessibility tools and features

## Architecture

### Window Management

```c
// Window manager core
struct WindowManager {
    struct Display *display;
    struct Window *focused_window;
    struct Window *stacking_order[MAX_WINDOWS];
    int window_count;
    
    void (*layout_windows)(struct WindowManager *wm);
    void (*focus_window)(struct WindowManager *wm, struct Window *window);
    void (*move_window)(struct WindowManager *wm, struct Window *window, int x, int y);
    void (*resize_window)(struct WindowManager *wm, struct Window *window, int width, int height);
};
```

### Compositor

```c
// Compositor for hardware acceleration
struct Compositor {
    struct Display *display;
    struct Surface *root_surface;
    struct Buffer *frame_buffer;
    
    void (*render_frame)(struct Compositor *comp);
    void (*composite_surface)(struct Compositor *comp, struct Surface *surface);
    void (*apply_effects)(struct Compositor *comp, struct Surface *surface);
    void (*present_frame)(struct Compositor *comp);
};
```

### Display Server

```c
// Wayland display server
struct DisplayServer {
    struct wl_display *display;
    struct wl_compositor *compositor;
    struct wl_shell *shell;
    
    void (*handle_client)(struct DisplayServer *server, struct wl_client *client);
    void (*handle_resource)(struct DisplayServer *server, struct wl_resource *resource);
    void (*handle_event)(struct DisplayServer *server, struct wl_event *event);
};
```

## Window Management

### Tiling Layouts

- **Master-Stack** - Classic tiling layout with master and stack areas
- **Columns** - Vertical column layout
- **Rows** - Horizontal row layout
- **Grid** - Grid-based tiling layout
- **Spiral** - Spiral tiling layout
- **Center Master** - Center-focused tiling layout
- **Fibonacci** - Fibonacci sequence tiling layout

### Floating Windows

- **Floating Mode** - Windows can float freely
- **Snapping** - Snap windows to edges and corners
- **Tiling Hints** - Hints for optimal window placement
- **Workspace** - Multiple workspaces for window organization
- **Tags** - Tag-based window organization
- **Scratchpad** - Hidden windows for quick access

### Window Operations

- **Move** - Move windows with mouse or keyboard
- **Resize** - Resize windows with mouse or keyboard
- **Minimize** - Minimize windows to taskbar
- **Maximize** - Maximize windows to fill screen
- **Fullscreen** - Fullscreen mode for windows
- **Close** - Close windows gracefully
- **Focus** - Focus management and switching

## Application Launcher

### Features

- **Fuzzy Search** - Fast fuzzy search for applications
- **Categories** - Application categories and filtering
- **Recent Apps** - Recently used applications
- **Favorites** - Favorite applications for quick access
- **Commands** - System commands and shortcuts
- **Files** - File search and opening
- **Calculations** - Inline calculations
- **Units** - Unit conversion
- **Weather** - Weather information
- **Clipboard** - Clipboard history

### Interface

```
┌─────────────────────────────────────┐
│  🔍 Search applications...          │
├─────────────────────────────────────┤
│  📁 Files                           │
│  🖥️  System                          │
│  🌐 Internet                        │
│  🎮 Games                           │
│  🎨 Graphics                        │
│  🎵 Audio                           │
│  🎬 Video                           │
│  📚 Office                           │
│  🛠️  Development                     │
│  ⚙️  Settings                        │
└─────────────────────────────────────┘
```

## System Settings

### Display Settings

- **Resolution** - Screen resolution and scaling
- **Refresh Rate** - Display refresh rate
- **Brightness** - Brightness control
- **Night Light** - Blue light filter
- **Color Profile** - Color profile management
- **Multi-Monitor** - Multi-monitor configuration
- **Rotation** - Screen rotation
- **Mirror** - Screen mirroring

### Input Settings

- **Keyboard** - Keyboard layout and shortcuts
- **Mouse** - Mouse sensitivity and acceleration
- **Touchpad** - Touchpad configuration
- **Stylus** - Stylus and pen input
- **Accessibility** - Accessibility features
- **Input Methods** - Input method editors
- **Hot Corners** - Hot corner actions
- **Gestures** - Touchpad gestures

### Sound Settings

- **Output** - Audio output device selection
- **Input** - Audio input device selection
- **Volume** - Volume control and mixer
- **Profiles** - Audio profiles for different scenarios
- **Effects** - Audio effects and processing
- **Microphone** - Microphone configuration
- **Notifications** - Notification sounds
- **System Sounds** - System event sounds

### Network Settings

- **Wi-Fi** - Wi-Fi configuration and management
- **Ethernet** - Ethernet configuration
- **Bluetooth** - Bluetooth device management
- **VPN** - VPN configuration
- **Firewall** - Firewall settings
- **DNS** - DNS configuration
- **Proxy** - Proxy settings
- **Network Profiles** - Network profiles for different locations

### Power Settings

- **Power Profiles** - Power saving profiles
- **Screen Timeout** - Screen timeout settings
- **Sleep** - Sleep and hibernation settings
- **Battery** - Battery monitoring and management
- **Thermal** - Thermal management
- **Performance** - Performance mode selection
- **Wake on LAN** - Wake on LAN settings
- **Auto Login** - Automatic login settings

## Theming

### Theme Engine

```css
/* SigmaOS theme variables */
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  --color-danger: #dc3545;
  --color-warning: #ffc107;
  --color-info: #17a2b8;
  
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-tertiary: #e9ecef;
  
  --text-primary: #212529;
  --text-secondary: #6c757d;
  --text-tertiary: #adb5bd;
  
  --border-primary: #dee2e6;
  --border-secondary: #ced4da;
  
  --shadow-sm: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  --shadow-md: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  --shadow-lg: 0 1rem 3rem rgba(0, 0, 0, 0.175);
}

/* Dark theme */
[data-theme="dark"] {
  --bg-primary: #1a1a1a;
  --bg-secondary: #2d2d2d;
  --bg-tertiary: #404040;
  
  --text-primary: #ffffff;
  --text-secondary: #b3b3b3;
  --text-tertiary: #808080;
  
  --border-primary: #404040;
  --border-secondary: #505050;
}
```

### Customization

- **Colors** - Custom color schemes
- **Fonts** - Font family and size
- **Icons** - Icon themes and styles
- **Cursors** - Custom cursor themes
- **Wallpapers** - Wallpaper management
- **Transparency** - Transparency effects
- **Animations** - Animation speed and effects
- **Layout** - Panel and widget layout

## Widgets

### System Widgets

- **Clock** - Clock and calendar widget
- **Weather** - Weather information widget
- **System Monitor** - CPU, memory, and disk usage
- **Network Monitor** - Network usage and status
- **Battery** - Battery status and charging
- **Media Player** - Media playback controls
- **Calendar** - Calendar events and reminders
- **Notes** - Quick notes and todo lists

### Productivity Widgets

- **Task Manager** - Task and project management
- **Pomodoro** - Pomodoro timer and focus
- **Habit Tracker** - Habit tracking and streaks
- **Journal** - Daily journal and notes
- **Goals** - Goal setting and tracking
- **Finance** - Expense tracking and budgeting
- **Health** - Health and fitness tracking
- **Reading** - Reading list and progress

### Information Widgets

- **RSS Reader** - RSS feed reader
- **News** - News aggregation
- **Social Media** - Social media feeds
- **Stock Ticker** - Stock market information
- **Crypto** - Cryptocurrency prices
- **Sports** - Sports scores and news
- **Traffic** - Traffic and commute information
- **Transit** - Public transit information

## Notifications

### Notification Types

- **System** - System notifications and alerts
- **Application** - Application notifications
- **Messages** - Instant messages and chat
- **Email** - Email notifications
- **Calendar** - Calendar reminders
- **Media** - Media playback notifications
- **Updates** - Software update notifications
- **Security** - Security alerts and warnings

### Notification Features

- **Rich Content** - Rich notification content with images
- **Actions** - Quick action buttons
- **History** - Notification history and archive
- **Do Not Disturb** - Do not disturb mode
- **Focus** - Focus mode for reduced distractions
- **Sounds** - Custom notification sounds
- **Vibration** - Vibration feedback
- **Preview** - Notification preview settings

## Multi-Monitor Support

### Configuration

- **Per-Monitor Settings** - Different settings per monitor
- **Arrangement** - Monitor arrangement and positioning
- **Scaling** - Per-monitor scaling settings
- **Refresh Rate** - Per-monitor refresh rate
- **Orientation** - Monitor orientation settings
- **Primary Monitor** - Primary monitor selection
- **Taskbar** - Taskbar on all monitors or primary only
- **Wallpaper** - Different wallpapers per monitor

### Features

- **Mixed DPI** - Support for different DPI monitors
- **Hot Plug** - Hot plug and unplug support
- **Mirror Mode** - Screen mirroring mode
- **Extended Mode** - Extended desktop mode
- **Clone Mode** - Clone screen mode
- **Rotation** - Per-monitor rotation
- **Brightness** - Per-monitor brightness
- **Color Profile** - Per-monitor color profiles

## Accessibility

### Visual Accessibility

- **High Contrast** - High contrast themes
- **Large Text** - Large text and UI scaling
- **Screen Reader** - Screen reader support
- **Magnifier** - Screen magnifier
- **Color Blind** - Color blind friendly themes
- **Reduced Motion** - Reduced motion animations
- **Focus Indicators** - Enhanced focus indicators
- **Keyboard Navigation** - Full keyboard navigation

### Motor Accessibility

- **Sticky Keys** - Sticky keys for modifier keys
- **Slow Keys** - Slow keys for deliberate typing
- **Bounce Keys** - Bounce keys to prevent repeated keys
- **Mouse Keys** - Mouse control via keyboard
- **Dwell Clicking** - Dwell clicking for motor impairments
- **Eye Tracking** - Eye tracking support
- **Switch Access** - Switch access support
- **Voice Control** - Voice control support

### Hearing Accessibility

- **Visual Alerts** - Visual alerts for audio events
- **Closed Captions** - Closed captions for media
- **Sound Amplification** - Sound amplification
- **Audio Description** - Audio description support
- **Hearing Aid** - Hearing aid compatibility
- **Mono Audio** - Mono audio output
- **Balance** - Audio balance control
- **Equalizer** - Audio equalizer

## Performance

### Optimization

- **GPU Acceleration** - Hardware-accelerated rendering
- **Compositing** - Efficient compositing pipeline
- **Memory Management** - Efficient memory usage
- **CPU Optimization** - CPU usage optimization
- **I/O Optimization** - I/O performance optimization
- **Startup Time** - Fast startup time
- **Resource Usage** - Low resource usage
- **Battery Life** - Battery life optimization

### Monitoring

- **Performance Metrics** - Real-time performance metrics
- **Resource Usage** - CPU, memory, and disk usage
- **Thermal Monitoring** - Temperature monitoring
- **Power Usage** - Power consumption monitoring
- **Network Usage** - Network bandwidth monitoring
- **Frame Rate** - Frame rate monitoring
- **Latency** - Input latency monitoring
- **Jank** - Animation jank detection

## Usage

```bash
# Start desktop environment
sigmaos-desktop start --session wayland

# Switch to different session
sigmaos-desktop session switch --type x11

# Configure display settings
sigmaos-desktop display set --resolution 1920x1080 --refresh-rate 60

# Change theme
sigmaos-desktop theme set --name sigmaos-dark --accent #007bff

# Add widget
sigmaos-desktop widget add --type clock --position top-right

# Configure notification
sigmaos-desktop notification set --dnd on --sound off
```

## Configuration

```json
{
  "desktop_environment": {
    "session": "wayland",
    "window_manager": "hyprland",
    "compositor": "hyprland",
    "display_server": "wayland",
    "shell": "ags",
    "launcher": "walker",
    "settings": "gnome-control-center",
    "notifications": "dunst",
    "theming": "matugen",
    "widgets": [
      "clock",
      "weather",
      "system-monitor",
      "network-monitor",
      "battery"
    ],
    "accessibility": {
      "screen_reader": false,
      "high_contrast": false,
      "large_text": false,
      "reduce_motion": false
    },
    "multi_monitor": {
      "enabled": true,
      "taskbar": "all",
      "wallpaper": "per-monitor"
    }
  }
}
```

## Troubleshooting

### Common Issues

**Display not working:**
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

## References

- [Wayland Protocol](https://wayland.freedesktop.org/)
- [X11 Protocol](https://www.x.org/releases/current/doc/xproto/x11protocol.html)
- [Hyprland](https://hyprland.org/)
- [Sway](https://swaywm.org/)
- [i3](https://i3wm.org/)
- [GNOME](https://www.gnome.org/)
- [KDE Plasma](https://kde.org/plasma-desktop/)
