const mongoose = require("mongoose");

// Connect to MongoDB
mongoose.connect("mongodb://localhost:27017/mern_app", {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log("MongoDB Connected"))
  .catch(err => console.log(err));

// Define Schema (for consistency)
const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    age: Number,
    role: String
});

// Create Model
const User = mongoose.model("User", userSchema);

// CRUD Operations
async function performCRUD() {
    try {
        // 1. Create: Insert Sample Data
        await User.insertMany([
            { name: "John Doe", email: "john@example.com", age: 30, role: "admin" },
            { name: "Alice Smith", email: "alice@example.com", age: 25, role: "user" },
            { name: "Bob Brown", email: "bob@example.com", age: 35, role: "moderator" }
        ]);
        console.log("Sample Users Inserted");

        // 2. Read: Fetch All Users
        console.log("\nAll Users:");
        console.log(await User.find());

        // 2. Read: Query Specific Users (age > 25, role = "admin")
        console.log("\nUsers with age > 25:");
        console.log(await User.find({ age: { $gt: 25 } }));

        console.log("\nAdmins:");
        console.log(await User.find({ role: "admin" }));

        // 2. Read: Sorting and Pagination (Sort by age descending, limit 2)
        console.log("\nSorted Users (by age, descending):");
        console.log(await User.find().sort({ age: -1 }).limit(2));

        // 3. Update: Update a Single User (Change Alice's role to admin)
        await User.updateOne({ name: "Alice Smith" }, { $set: { role: "admin" } });
        console.log("\nUpdated Alice's Role to Admin");

        // 3. Update: Increment age for all users
        await User.updateMany({}, { $inc: { age: 1 } });
        console.log("\nIncreased age for all users");

        // 4. Delete: Remove a Single User (Bob)
        await User.deleteOne({ name: "Bob Brown" });
        console.log("\nDeleted Bob");

        // 4. Delete: Remove Multiple Users (age > 50)
        await User.deleteMany({ age: { $gt: 50 } });
        console.log("\nDeleted Users with Age > 50");

        // 4. Drop Collection (⚠️ Be careful)
        // await User.collection.drop();
        // console.log("\nUsers collection dropped");

        mongoose.connection.close(); // Close the connection
    } catch (error) {
        console.error(error);
    }
}

// Execute CRUD operations
performCRUD();
