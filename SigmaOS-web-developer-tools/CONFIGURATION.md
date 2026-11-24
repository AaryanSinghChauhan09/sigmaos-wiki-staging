# Web Developer Tools Configuration

## Editor Configuration

### VSCode Settings

```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "Fira Code",
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "workbench.colorTheme": "SigmaOS Dark",
  "terminal.integrated.defaultProfile.linux": "bash",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000
}
```

### Extension Configuration

```json
{
  "extensions": {
    "eslint": {
      "enable": true,
      "configFile": ".eslintrc.js"
    },
    "prettier": {
      "printWidth": 100,
      "tabWidth": 2,
      "useTabs": false,
      "semi": true,
      "singleQuote": true,
      "trailingComma": "es5"
    },
    "typescript": {
      "validate.enable": true,
      "tsdk": "node_modules/typescript/lib"
    }
  }
}
```

## Debugging Configuration

### Launch Configuration

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "Launch Chrome",
      "url": "http://localhost:3000",
      "webRoot": "${workspaceFolder}",
      "sourceMaps": true,
      "runtimeArgs": [
        "--disable-web-security"
      ]
    },
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Server",
      "program": "${workspaceFolder}/server.js",
      "cwd": "${workspaceFolder}",
      "env": {
        "NODE_ENV": "development"
      }
    }
  ]
}
```

### Breakpoint Configuration

```javascript
// Conditional breakpoints
if (user.isAdmin) {
  debugger; // Only breaks for admin users
}

// Log points
console.log(`User: ${user.name}, Action: ${action}`);

// Exception breakpoints
try {
  riskyOperation();
} catch (error) {
  console.error('Operation failed:', error);
}
```

## Testing Configuration

### Jest Configuration

```javascript
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

### Cypress Configuration

```javascript
module.exports = {
  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: 'cypress/integration/**/*.spec.{js,jsx,ts,tsx}',
    supportFile: 'cypress/support/index.js',
    video: false,
    screenshotOnRunFailure: false,
    viewportWidth: 1280,
    viewportHeight: 720
  }
};
```

## Build Configuration

### Webpack Configuration

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    clean: true
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader'
        ]
      },
      {
        test: /\.(png|jpg|jpeg|gif|svg)$/,
        type: 'asset/resource'
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css'
    })
  ],
  optimization: {
    splitChunks: {
      chunks: 'all'
    }
  },
  devServer: {
    port: 3000,
    hot: true,
    open: true,
    historyApiFallback: true
  }
};
```

### Vite Configuration

```javascript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@mui/material', '@emotion/react']
        }
      }
    }
  }
});
```

## Performance Configuration

### Lighthouse Configuration

```javascript
// lighthouse.config.js
module.exports = {
  extends: 'lighthouse:default',
  settings: {
    onlyCategories: ['performance', 'accessibility', 'best-practices', 'seo'],
    formFactor: 'mobile',
    screenEmulation: {
      mobile: true,
      width: 360,
      height: 640,
      deviceScaleFactor: 2,
      disabled: false
    }
  },
  audits: {
    'uses-http2': 'off',
    'uses-rel-preconnect': 'warn'
  }
};
```

### Bundle Analyzer

```javascript
// webpack.config.js
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      reportFilename: 'bundle-report.html',
      openAnalyzer: false
    })
  ]
};
```

## Security Configuration

### Content Security Policy

```javascript
// helmet.js configuration
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "https://api.example.com"],
      fontSrc: ["'self'"],
      objectSrc: ["'none'"],
      mediaSrc: ["'self'"],
      frameSrc: ["'none'"]
    }
  }
}));
```

### CORS Configuration

```javascript
const cors = require('cors');

app.use(cors({
  origin: ['http://localhost:3000', 'https://app.example.com'],
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

## Environment Configuration

### Environment Variables

```bash
# .env.development
NODE_ENV=development
API_URL=http://localhost:8080
DATABASE_URL=sqlite:./dev.db
SECRET_KEY=dev-secret-key
DEBUG=true
LOG_LEVEL=debug
```

```bash
# .env.production
NODE_ENV=production
API_URL=https://api.example.com
DATABASE_URL=postgresql://user:pass@host:5432/db
SECRET_KEY=production-secret-key
DEBUG=false
LOG_LEVEL=info
```

### Configuration Management

```javascript
// config.js
const config = {
  development: {
    apiUrl: process.env.API_URL || 'http://localhost:8080',
    databaseUrl: process.env.DATABASE_URL || 'sqlite:./dev.db',
    secretKey: process.env.SECRET_KEY || 'dev-secret',
    debug: true,
    logLevel: 'debug'
  },
  production: {
    apiUrl: process.env.API_URL,
    databaseUrl: process.env.DATABASE_URL,
    secretKey: process.env.SECRET_KEY,
    debug: false,
    logLevel: 'info'
  }
};

module.exports = config[process.env.NODE_ENV || 'development'];
```

## Troubleshooting

### Common Issues

**Build fails:**
```bash
# Check for syntax errors
npm run lint

# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Check for dependency conflicts
npm ls
```

**Dev server won't start:**
```bash
# Check port availability
lsof -i :3000

# Kill process using port
kill -9 $(lsof -t -i:3000)

# Start with different port
npm start -- --port 3001
```

**Hot reload not working:**
```bash
# Check file watcher limits
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Restart dev server
npm run dev -- --force
```

## Best Practices

### Code Organization

- Use consistent file naming conventions
- Group related files in directories
- Use index files for exports
- Keep components small and focused
- Separate business logic from UI
- Use TypeScript for type safety

### Performance

- Use code splitting for large applications
- Implement lazy loading for routes
- Optimize images and assets
- Use CDN for static assets
- Minimize bundle size
- Enable compression
- Use service workers for caching

### Security

- Validate all user input
- Use HTTPS in production
- Implement proper authentication
- Use environment variables for secrets
- Keep dependencies updated
- Run security audits regularly
- Use security headers

### Testing

- Write unit tests for components
- Write integration tests for features
- Write E2E tests for user flows
- Maintain test coverage above 80%
- Use test-driven development
- Mock external dependencies
- Test edge cases and error conditions
