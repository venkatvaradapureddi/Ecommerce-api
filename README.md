# ecommerce-api
# 🛍️ eCommerce Products API

This is a simple REST API built using **Django Rest Framework (DRF)** to serve product data for an eCommerce frontend.

## 🌐 Live API URLs

- 🔹 **Get All Products**  
  [http://venkat123.pythonanywhere.com/api/products/](http://venkat123.pythonanywhere.com/api/products/)

- 🔹 **Filter Products by Category** (example: Men's Clothing)  
  [http://venkat123.pythonanywhere.com/api/products/?category=men%27s%20clothing](http://venkat123.pythonanywhere.com/api/products/?category=men%27s%20clothing)

- 🔹 **Get All Categories**  
  [http://venkat123.pythonanywhere.com/api/products/categories](http://venkat123.pythonanywhere.com/api/products/categories)

## 📦 Features

- View all products
- Filter products by category
- View all available categories

## 🔧 Example Usage

### ✅ Get all products
```http
GET http://venkat123.pythonanywhere.com/api/products/
