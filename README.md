# eCommerce Website with Payment Integration

## 📌 Overview
This is a fully functional eCommerce website that allows users to browse products, add items to the cart, and securely complete transactions using integrated payment gateways. The platform provides a seamless shopping experience with user authentication, order tracking, and a responsive design.

## 🚀 Features
- User authentication (Signup/Login)
- Product listing and search functionality
- Shopping cart and checkout process
- Secure payment gateway integration
- Order management and tracking
- Responsive and user-friendly UI

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript, React.js
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Payment Gateway**: Stripe / Razorpay / PayPal (configurable)

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-website.git
   cd ecommerce-website
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up environment variables (`.env` file):
   ```plaintext
   MONGO_URI=your_mongodb_connection_string
   STRIPE_SECRET_KEY=your_stripe_secret_key
   JWT_SECRET=your_jwt_secret
   ```
4. Start the backend server:
   ```bash
   npm run server
   ```
5. Start the frontend:
   ```bash
   cd client
   npm install
   npm start
   ```

## 🔗 API Endpoints
| Method | Endpoint           | Description |
|--------|-------------------|-------------|
| GET    | /api/products     | Fetch all products |
| GET    | /api/products/:id | Fetch product by ID |
| POST   | /api/users/login  | User login |
| POST   | /api/users/signup | User registration |
| POST   | /api/orders       | Create new order |

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

## ✨ Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

Home
![image](https://github.com/user-attachments/assets/8f07dfc3-337e-4a4e-9683-93f0685b9a9e)
Payment 
![image](https://github.com/user-attachments/assets/48856cc4-5e90-48b0-b1a8-7986ffd417ec)

