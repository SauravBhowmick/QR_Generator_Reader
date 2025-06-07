# Product QR Code Generator 📱

A Python library for generating QR codes from product information. Perfect for inventory management, product catalogs, retail applications, and customer information sharing.

## ✨ Features

- 🏷️ **Structured Product Data**: Support for comprehensive product information including name, price, description, SKU, manufacturer, and more
- 📊 **Multiple Output Formats**: Generate QR codes in JSON, human-readable text, or URL formats
- 🎨 **Customizable QR Codes**: Adjustable size, error correction, and styling options
- 📱 **Mobile-Friendly**: Generated QR codes work with any standard QR code scanner
- 🔧 **Easy Integration**: Simple API for embedding into existing applications
- 📝 **Custom Data Support**: Create QR codes from any custom text data

## 🚀 Quick Start

### Installation

```bash
pip install qrcode[pil]
```

### Basic Usage

```python
from product_qr_generator import ProductQRGenerator

# Create generator instance
generator = ProductQRGenerator()

# Create product information
product = generator.create_product_info(
    name="Wireless Bluetooth Headphones",
    price=89.99,
    description="High-quality wireless headphones with noise cancellation",
    category="Electronics",
    sku="WBH-001",
    manufacturer="TechSound"
)

# Generate QR code
generator.generate_qr_code(product, "my_product_qr.png", "text")
```

## 📋 API Reference

### ProductQRGenerator Class

#### `create_product_info(name, price, description, category, **kwargs)`

Creates a structured product information dictionary.

**Parameters:**
- `name` (str): Product name
- `price` (float): Product price
- `description` (str): Product description
- `category` (str): Product category
- `sku` (str, optional): Stock Keeping Unit
- `manufacturer` (str, optional): Manufacturer name
- `weight` (str, optional): Product weight
- `dimensions` (str, optional): Product dimensions
- `url` (str, optional): Product URL or website

**Returns:** Dictionary containing structured product information

#### `generate_qr_code(product_info, filename, format_type)`

Generates a QR code from product information.

**Parameters:**
- `product_info` (dict): Product information dictionary
- `filename` (str): Output filename (default: "product_qr.png")
- `format_type` (str): Output format - "json", "text", or "url"

**Returns:** Tuple of (QR code image, encoded data string)

#### `create_custom_qr(data, filename)`

Creates a QR code from custom text data.

**Parameters:**
- `data` (str): Custom text data to encode
- `filename` (str): Output filename (default: "custom_qr.png")

## 💡 Usage Examples

### Electronics Product

```python
generator = ProductQRGenerator()

electronics = generator.create_product_info(
    name="Smartphone XYZ",
    price=599.99,
    description="Latest flagship smartphone with advanced camera",
    category="Electronics",
    sku="SPH-XYZ-128",
    manufacturer="TechCorp",
    weight="175g",
    dimensions="15.8 x 7.6 x 0.8 cm",
    url="https://store.example.com/smartphone-xyz"
)

# Generate different format types
generator.generate_qr_code(electronics, "phone_json.png", "json")
generator.generate_qr_code(electronics, "phone_text.png", "text")
generator.generate_qr_code(electronics, "phone_url.png", "url")
```

### Clothing Product

```python
clothing = generator.create_product_info(
    name="Organic Cotton T-Shirt",
    price=29.99,
    description="Eco-friendly 100% organic cotton t-shirt",
    category="Clothing",
    sku="TSHIRT-ORG-M-BLU",
    manufacturer="EcoFashion"
)

generator.generate_qr_code(clothing, "tshirt_qr.png", "text")
```

### Custom Contact Information

```python
contact_info = """
Contact: John Smith
Company: ABC Corporation
Phone: +1-555-0123
Email: john.smith@abc.com
Website: www.abc.com
"""

generator.create_custom_qr(contact_info, "contact_qr.png")
```

## 📊 QR Code Formats

### JSON Format
Structured data perfect for applications and databases:
```json
{
  "name": "Product Name",
  "price": 99.99,
  "description": "Product description",
  "category": "Category",
  "sku": "PRD-001",
  "timestamp": "2024-06-07 14:30:00"
}
```

### Text Format
Human-readable format ideal for customer scanning:
```
Product: Wireless Headphones
Price: $89.99
Category: Electronics
Description: High-quality wireless headphones
SKU: WBH-001
Generated: 2024-06-07 14:30:00
```

### URL Format
Direct link format for web integration:
```
https://store.example.com/product/wbh-001
```

## 🔧 Customization

### QR Code Settings

You can customize QR code appearance by modifying the generator settings:

```python
generator = ProductQRGenerator()
generator.qr.version = 2  # Larger QR code
generator.qr.error_correction = qrcode.constants.ERROR_CORRECT_H  # High error correction
generator.qr.box_size = 15  # Larger boxes
generator.qr.border = 6  # Larger border
```

### Custom Styling

```python
# Generate with custom colors
qr_img = generator.qr.make_image(fill_color="blue", back_color="yellow")
qr_img.save("custom_colored_qr.png")
```

## 🛠️ Requirements

- Python 3.6+
- qrcode[pil] library
- PIL (Python Imaging Library)

## 📱 Use Cases

- **Retail & E-commerce**: Product information sharing
- **Inventory Management**: Quick product lookups
- **Marketing**: Product promotions and details
- **Restaurants**: Menu items and nutritional information  
- **Manufacturing**: Part specifications and tracking
- **Events**: Exhibitor and product information
- **Real Estate**: Property details and contact info

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page for existing problems
2. Create a new issue with detailed information about your problem
3. Include your Python version and operating system details

## 🔮 Roadmap

- [ ] Support for batch QR code generation
- [ ] Integration with barcode formats
- [ ] Web interface for non-technical users
- [ ] Database integration examples
- [ ] REST API wrapper
- [ ] Advanced styling options
- [ ] QR code validation and verification tools

## 📸 Screenshots

### Generated QR Code Examples

| Format | Example |
|--------|---------|
| JSON Format | ![JSON QR](examples/json_qr_example.png) |
| Text Format | ![Text QR](examples/text_qr_example.png) |
| URL Format | ![URL QR](examples/url_qr_example.png) |

---

Made with ❤️ for developers who need simple, effective QR code generation for product information.
