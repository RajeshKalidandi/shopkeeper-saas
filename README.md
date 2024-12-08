# ShopKeeper Pro - All-in-One Business Management Suite

Empower local shopkeepers in India to streamline their business operations, reduce manual errors, and increase profitability.

## Features

### Implemented
- Custom User Authentication
  - Email-based authentication
  - Shop profile management
  - Subscription management

- Inventory Management
  - Product categories
  - Product information with SKU and barcode
  - Stock tracking with transaction history
  - Low stock alerts

- Billing System
  - Invoice generation
  - Multiple payment methods (Cash, UPI, Card, Store Credit)
  - Invoice items with tax and discount
  - Payment tracking

- Customer Relationship Management (CRM)
  - Customer database
  - Interaction tracking
  - Loyalty program
  - Follow-up management

### Upcoming Features
- Dashboard Analytics
- Supplier Management
- Financial Reports
- SMS/Email Notifications
- Mobile App
- Multi-language Support
- Offline Mode
- Data Backup

## Tech Stack
- **Backend**: Django 5.0
- **Database**: PostgreSQL
- **API**: Django REST Framework
- **Frontend** (Coming Soon): React.js
- **Payment Gateway**: Stripe (with UPI integration)
- **AI Features**: TensorFlow for predictive analytics

## Project Structure
```
shopkeeper-saas/
├── accounts/          # User authentication and shop profiles
├── inventory/         # Product and stock management
├── billing/          # Invoice and payment processing
├── crm/              # Customer relationship management
└── shopkeeper_pro/   # Project settings and configuration
```

## Database Schema
- **Accounts**
  - CustomUser
  - ShopProfile

- **Inventory**
  - Category
  - Product
  - Stock

- **Billing**
  - Invoice
  - InvoiceItem
  - Payment

- **CRM**
  - Customer
  - CustomerInteraction
  - Loyalty

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL 17+
- Node.js 18+ (for frontend - coming soon)

### Installation
1. Clone the repository
```bash
git clone https://github.com/RajeshKalidandi/shopkeeper-saas.git
cd shopkeeper-saas
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
Create a `.env` file in the root directory with:
```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/shopkeeper_db
STRIPE_SECRET_KEY=your_stripe_key
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run development server
```bash
python manage.py runserver
```

## API Documentation
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Rajesh Kalidandi - [GitHub](https://github.com/RajeshKalidandi)
