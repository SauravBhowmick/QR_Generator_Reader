import qrcode
from PIL import Image
import json
from datetime import datetime

class ProductQRGenerator:
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    
    def create_product_info(self, name, price, description, category, sku=None, 
                          manufacturer=None, weight=None, dimensions=None, url=None):
        """
        Create a structured product information dictionary
        """
        product_info = {
            "name": name,
            "price": price,
            "description": description,
            "category": category,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add optional fields if provided
        if sku:
            product_info["sku"] = sku
        if manufacturer:
            product_info["manufacturer"] = manufacturer
        if weight:
            product_info["weight"] = weight
        if dimensions:
            product_info["dimensions"] = dimensions
        if url:
            product_info["url"] = url
            
        return product_info
    
    def generate_qr_code(self, product_info, filename="product_qr.png", format_type="json"):
        """
        Generate QR code from product information
        
        Args:
            product_info: Dictionary containing product details
            filename: Output filename for the QR code image
            format_type: Format to encode data ('json', 'text', 'url')
        """
        # Clear previous data
        self.qr.clear()
        
        # Format the data based on type
        if format_type == "json":
            data = json.dumps(product_info, indent=2)
        elif format_type == "text":
            data = self.format_as_text(product_info)
        elif format_type == "url" and "url" in product_info:
            data = product_info["url"]
        else:
            data = json.dumps(product_info)
        
        # Add data to QR code
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        # Create QR code image
        qr_img = self.qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        qr_img.save(filename)
        print(f"QR code saved as: {filename}")
        
        return qr_img, data
    
    def format_as_text(self, product_info):
        """
        Format product information as readable text
        """
        text = f"Product: {product_info['name']}\n"
        text += f"Price: ${product_info['price']}\n"
        text += f"Category: {product_info['category']}\n"
        text += f"Description: {product_info['description']}\n"
        
        if "sku" in product_info:
            text += f"SKU: {product_info['sku']}\n"
        if "manufacturer" in product_info:
            text += f"Manufacturer: {product_info['manufacturer']}\n"
        if "weight" in product_info:
            text += f"Weight: {product_info['weight']}\n"
        if "dimensions" in product_info:
            text += f"Dimensions: {product_info['dimensions']}\n"
        if "url" in product_info:
            text += f"More Info: {product_info['url']}\n"
            
        text += f"Generated: {product_info['timestamp']}"
        return text
    
    def create_custom_qr(self, data, filename="custom_qr.png"):
        """
        Create QR code from custom data string
        """
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        qr_img = self.qr.make_image(fill_color="black", back_color="white")
        qr_img.save(filename)
        print(f"Custom QR code saved as: {filename}")
        
        return qr_img

# Example usage and demonstration
def main():
    # Create QR generator instance
    generator = ProductQRGenerator()
    
    # Example 1: Electronics product
    print("=== Example 1: Electronics Product ===")
    product1 = generator.create_product_info(
        name="Wireless Bluetooth Headphones",
        price=89.99,
        description="High-quality wireless headphones with noise cancellation",
        category="Electronics",
        sku="WBH-001",
        manufacturer="TechSound",
        weight="250g",
        dimensions="18 x 15 x 8 cm",
        url="https://example.com/product/wbh-001"
    )
    
    # Generate QR codes in different formats
    generator.generate_qr_code(product1, "headphones_json.png", "json")
    generator.generate_qr_code(product1, "headphones_text.png", "text")
    generator.generate_qr_code(product1, "headphones_url.png", "url")
    
    # Example 2: Clothing product
    print("\n=== Example 2: Clothing Product ===")
    product2 = generator.create_product_info(
        name="Cotton T-Shirt",
        price=24.99,
        description="100% organic cotton t-shirt, comfortable fit",
        category="Clothing",
        sku="CT-M-BLU",
        manufacturer="EcoWear",
        weight="180g",
        dimensions="Size M: Chest 102cm, Length 71cm"
    )
    
    generator.generate_qr_code(product2, "tshirt_qr.png", "text")
    
    # Example 3: Custom data
    print("\n=== Example 3: Custom Data ===")
    custom_data = "Contact: John Doe\nPhone: +1-555-0123\nEmail: john@example.com\nCompany: ABC Corp"
    generator.create_custom_qr(custom_data, "contact_qr.png")
    
    # Display the JSON data that would be encoded
    print("\n=== Product 1 JSON Data ===")
    print(json.dumps(product1, indent=2))

if __name__ == "__main__":
    # Install required packages first:
    # pip install qrcode[pil]
    
    print("Product QR Code Generator")
    print("========================")
    print("Make sure to install required packages:")
    print("pip install qrcode[pil]")
    print()
    
    main()