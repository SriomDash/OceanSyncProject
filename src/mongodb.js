const mongoose = require('mongoose');
mongoose.connect("mongodb://localhost:27017/mydb")
.then(() => {
    console.log('mongodb connected')
}).catch((err) => {
    console.log('mongodb not connected')
});

const loginshcema = new mongoose.Schema({
    Name:{
        type:String,
        required:true
    },
    City:{
        type:String,
        required:true
    },
    Type:{
        type:String,
        required:true
    },
    Quantity:{
        type:String,
        required:true
    },
    Location:{
        type:String,
        required:true
    },
    Price:{
        type:String,
        required:true
    }
})

const collection = new mongoose.model("collection1",loginshcema);
module.exports=collection;