const express = require('express');
const app = express();

const path = require('path');
const hbs = require('hbs');
const collection = require('./mongodb');
const templatepath = path.join(__dirname, '../templates');

app.use(express.json());
app.set('view engine', 'hbs');
app.set("views", templatepath);
app.use(express.static('public'));
app.use(express.urlencoded({ extended: false }));

// app.get('/home', (req, resp) => {
//     resp.render('home');
// });

app.get('/signup', (req, resp) => {
    resp.render('signup');
});

app.post('/signup', async (req, resp) => {
    const { Name, City, Type, Quantity, Location, Price } = req.body;

    try {
        const data = {
            Name,
            City,
            Type,
            Quantity,
            Location,
            Price
        };

        await collection.create(data);
        // resp.json({ message: "Signup successful" });
        resp.redirect('http://127.0.0.1:5500/index.html'); // Redirect to the home page
    } catch (error) {
        resp.status(500).json({ error: "Internal server error" });
    }
});

app.listen(5000, () => {
    console.log("Server is running on port 5000");
});
