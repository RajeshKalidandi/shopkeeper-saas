# ShopKeeper Pro - SaaS Application

A modern SaaS application designed to help local shopkeepers in India manage their business operations efficiently.

## Project Status

**Current Status**: Initial Development Phase
**Last Updated**: December 8, 2024

### Completed Features

#### Authentication System
- Modern login and registration pages with responsive design
- Form validation and error handling
- Session-based authentication with CSRF protection
- Protected routes and middleware implementation

#### Dashboard Layout
- Responsive sidebar navigation
- Modern dashboard shell with animations
- Stats cards with glassmorphism effects
- Mobile-friendly design

### Tech Stack

#### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Shadcn UI Components
- React Query for data fetching
- Axios for API communication

#### Backend
- Django 4.2
- Django REST Framework
- PostgreSQL
- Django CORS headers

### Project Structure

```
shopkeeper-saas/
├── frontend/               # Next.js frontend application
│   ├── src/
│   │   ├── app/           # Next.js app router pages
│   │   ├── components/    # Reusable React components
│   │   ├── lib/          # Utility functions and configurations
│   │   └── styles/       # Global styles
│   └── public/           # Static assets
│
├── accounts/             # Django user authentication app
├── inventory/           # Inventory management app
├── billing/            # Billing and invoicing app
└── crm/               # Customer relationship management app
```

### Setup Instructions

1. Clone the repository
```bash
git clone [repository-url]
cd shopkeeper-saas
```

2. Backend Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver 8080
```

3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3001
- Backend API: http://localhost:8080

### Next Steps

1. Implement core business features:
   - Inventory management system
   - Billing and invoicing
   - Customer management
   - Reports and analytics

2. Add additional features:
   - Multi-language support
   - Dark mode
   - Mobile app
   - Offline support

### Contributing

This project is currently in development. Feel free to submit issues and pull requests.

### License

[MIT License](LICENSE)
