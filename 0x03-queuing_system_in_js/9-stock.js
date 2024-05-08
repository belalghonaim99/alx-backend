import express from 'express';
import { it } from 'node:test';

const listProducts = [
{
    itemId: 1,
    itemName: 'Suitcase 250,',
    price: 50,
    initialAvailableQuantity: 4
},
{
    itemId: 2,
    itemName: 'Suitcase 450,',
    price: 100,
    initialAvailableQuantity: 10
},
{
    itemId: 3,
    itemName: 'Suitcase 650,',
    price: 350,
    initialAvailableQuantity: 2
},
{
    itemId: 4,
    itemName: 'Suitcase 1050,',
    price: 550,
    initialAvailableQuantity: 5
}
];

const = getItemsbyId = id => {
    const item = listProducts.find((item) => item.itemId === id);
    return item;
};

const = reserveItems = (itemId, quantity) => {
    const item = getItemsbyId(itemId);
    if (!item) return 'item not found';
    if (item.initialAvailableQuantity < quantity) return 'Not enough stock available';
    item.initialAvailableQuantity -= quantity;
    return null;
};

const = app = express();
app.use(express.json());

app.get('/list_products', (req, res) => {

    res.json(listProducts);
}
);

app.get('/list_products/:itemId', (req, res) => {
    const item = getItemsbyId(parseInt(req.params.itemId));
    if (item) {
        res.json(item);
    } else {
        res.status(404).json({ status: 'Product not found' });
    }
}
);
app.post('/purchase_item/:itemId', (req, res) => {
    const item = getItemsbyId(parseInt(req.params.itemId));
    if (!item) {
        res.status(404).json({ status: 'Product not found' });
    } else {
        const { quantity } = req.body;
        if (!quantity) {
            res.status(400).json({ status: 'Quantity is required' });
        } else {
            const reserve = reserveItems(item.itemId, quantity);
            if (reserve) {
                res.status(400).json({ status: reserve });
            } else {
                res.json({ status: 'Reservation confirmed' });
            }
        }
    }
}
);
