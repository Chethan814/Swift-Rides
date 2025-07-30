# SwiftRides - Car Rental Application

A Django-based car rental application deployed on Vercel.

## Features

- Car search and booking
- User authentication
- Admin panel
- Responsive design with Tailwind CSS

## Deployment on Vercel

### Prerequisites

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Make sure you have the following files in your project root:
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `build_files.sh` - Build script

### Deployment Steps

1. **Login to Vercel:**
```bash
vercel login
```

2. **Deploy the project:**
```bash
vercel
```

3. **For production deployment:**
```bash
vercel --prod
```

### Environment Variables

Set the following environment variables in your Vercel dashboard:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to 'False' for production
- `ALLOWED_HOSTS` - Your Vercel domain

### Important Notes

1. **Database**: This project uses SQLite for development. For production, consider using a cloud database like PostgreSQL.

2. **Static Files**: Static files are served using WhiteNoise middleware.

3. **Media Files**: Media files are stored locally. For production, consider using a cloud storage service.

## Local Development

1. **Clone the repository:**
```bash
git clone <repository-url>
cd SwiftRides
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create a superuser:**
```bash
python manage.py createsuperuser
```

6. **Run the development server:**
```bash
python manage.py runserver
```

## Project Structure

```
SwiftRides/
├── SwiftRides/          # Django project settings
├── home/               # Home app
├── user_profile/       # User management app
├── templates/          # HTML templates
├── static/            # Static files
├── media/             # User uploaded files
├── requirements.txt   # Python dependencies
├── vercel.json       # Vercel configuration
└── build_files.sh    # Build script
```

## Troubleshooting

### Common Issues

1. **404 Error**: Make sure your `vercel.json` is properly configured
2. **Static Files Not Loading**: Check if WhiteNoise is properly configured
3. **Database Issues**: Ensure your database is properly set up

### Vercel Logs

Check Vercel deployment logs for detailed error information:
```bash
vercel logs
``` 