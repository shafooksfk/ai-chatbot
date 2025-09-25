db = db.getSiblingDB("ecomdb");

db.products.insertMany([
  {
    product_id: "P1001",
    name: "Wireless Mouse",
    category: "Electronics",
    description: "Ergonomic wireless mouse",
    price: 25.99,
    attributes: { color: "black", battery: "AA" }
  },
  {
    product_id: "P2002",
    name: "Mechanical Keyboard",
    category: "Electronics",
    description: "Backlit mechanical keyboard",
    price: 100.50,
    attributes: { color: "white", switches: "blue" }
  },
  {
    product_id: "P3003",
    name: "Bluetooth Headphones",
    category: "Audio",
    description: "Noise-cancelling over-ear headphones",
    price: 64.99,
    attributes: { color: "black", battery_life: "20h" }
  }
]);

db.inventory.insertMany([
  { product_id: "P1001", location: "Warehouse A", stock: 120 },
  { product_id: "P2002", location: "Warehouse B", stock: 50 },
  { product_id: "P3003", location: "Warehouse A", stock: 75 }
]);
