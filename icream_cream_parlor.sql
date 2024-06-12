CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL,
    description TEXT,
    available BOOLEAN NOT NULL CHECK (available IN (0, 1))
);

-- Table for ingredient inventory
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL,
    quantity INTEGER NOT NULL
);

-- Table for customer flavor suggestions and allergy concerns
CREATE TABLE IF NOT EXISTS customer_suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    flavor_suggestion TEXT,
    allergy_concern TEXT
);

-- Table for user cart
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL
);

-- Table for allergens
CREATE TABLE IF NOT EXISTS allergens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    allergen_name TEXT NOT NULL UNIQUE
);

-- Sample data for seasonal flavors
INSERT INTO seasonal_flavors (flavor_name, description, available) VALUES
('Vanilla Delight', 'Classic vanilla flavor', 1),
('Mango Tango', 'Fresh mango ice cream', 0),
('Chocolate Bliss', 'Rich chocolate flavor', 1),
('Strawberry Dream', 'Sweet strawberry ice cream', 1),
('Mint Magic', 'Refreshing mint ice cream', 0),
('Caramel Swirl', 'Creamy caramel ice cream', 1);

-- Sample data for ingredient inventory
INSERT INTO ingredients (ingredient_name, quantity) VALUES
('Milk', 50),
('Sugar', 30),
('Cream', 20),
('Cocoa', 10),
('Strawberries', 15),
('Mint Leaves', 5),
('Caramel', 8);

-- Sample data for allergens
INSERT INTO allergens (allergen_name) VALUES
('Peanuts'),
('Lactose'),
('Gluten'),
('Tree Nuts'),
('Soy');

-- Sample data for customer suggestions and allergy concerns
INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concern) VALUES
('Hitesh','Banana Split','Dairy'),
('Hari', 'Blueberry Cheesecake', 'None'),
('Ravi', 'Lemon Sorbet', 'Gluten'),
('Ramu', 'Peach Cobbler', 'None');
