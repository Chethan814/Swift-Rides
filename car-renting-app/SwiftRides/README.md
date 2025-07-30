# SwiftRides - Car Rental Application

A Django-based car rental application with Tailwind CSS styling.

## Features

- Modern responsive design with Tailwind CSS
- Car search and booking functionality
- User authentication and profiles
- Admin panel for car management
- Mobile-friendly interface

## Vercel Deployment

### Prerequisites

1. **Vercel CLI** installed
2. **Git** repository set up
3. **Node.js** and **npm** (for Tailwind CSS build)

### Deployment Steps

1. **Clone and navigate to the project:**
   ```bash
   cd car-renting-app/SwiftRides
   ```

2. **Install dependencies locally (for testing):**
   ```bash
   pip install -r requirements.txt
   npm install
   ```

3. **Build Tailwind CSS locally:**
   ```bash
   python manage.py tailwind build
   ```

4. **Deploy to Vercel:**
   ```bash
   vercel
   ```

5. **Set environment variables in Vercel dashboard:**
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Your Vercel domain

### Environment Variables

Set these in your Vercel project settings:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app.vercel.app
```

## Important Notes

### Static Files Configuration

- Static files are served via WhiteNoise middleware
- Tailwind CSS is built during deployment
- Static files are collected to `staticfiles/` directory

### Build Process

The `build_files.sh` script handles:
1. Python dependencies installation
2. Node.js dependencies installation
3. Tailwind CSS build
4. Static files collection
5. Database migrations

### File Structure

```
SwiftRides/
├── static/                 # Static files (CSS, JS, images)
├── staticfiles/           # Collected static files (production)
├── templates/             # HTML templates
├── theme/                 # Tailwind CSS configuration
│   └── static_src/
│       ├── src/styles.css # Main CSS file
│       └── tailwind.config.js
├── vercel.json           # Vercel configuration
├── build_files.sh        # Build script
└── requirements.txt      # Python dependencies
```

## Troubleshooting

### Styling Issues

If styles are not loading:

1. **Check Vercel Build Logs:**
   ```bash
   vercel logs
   ```

2. **Verify Static Files:**
   - Check if `/static/test.css` is accessible
   - Look for the red test box on your website

3. **Check Tailwind Build:**
   - Ensure `python manage.py tailwind build` runs successfully
   - Check if Tailwind CSS is being generated

4. **Common Issues:**
   - **Missing Node.js dependencies**: Run `npm install` locally
   - **PostCSS configuration**: Ensure `postcss.config.js` is correct
   - **Static file routing**: Check `vercel.json` routes

### Quick Fix for Styling Issues

If styling still doesn't work:

1. **Force rebuild:**
   ```bash
   vercel --force
   ```

2. **Check file paths:**
   - Ensure all static file paths use forward slashes (`/`)
   - Verify `{% static %}` tags are correct

3. **Verify Tailwind CSS:**
   - Check if `{% tailwind_css %}` is in the template
   - Ensure Tailwind is loaded before other CSS

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   npm install
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Start development server:**
   ```bash
   python manage.py runserver
   ```

4. **Build Tailwind CSS (development):**
   ```bash
   python manage.py tailwind start
   ```

## Project Structure

- **`home/`**: Main app with views and models
- **`user_profile/`**: User authentication and profiles
- **`theme/`**: Tailwind CSS configuration
- **`templates/`**: HTML templates
- **`static/`**: Static files (CSS, JS, images)
- **`media/`**: User-uploaded files

## Support

For deployment issues:
1. Check Vercel build logs
2. Verify environment variables
3. Test static file serving
4. Ensure all dependencies are installed

For styling issues:
1. Verify Tailwind CSS build
2. Check static file paths
3. Ensure proper template inheritance
4. Test with the provided test elements 