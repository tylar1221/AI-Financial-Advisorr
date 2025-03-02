import mongoose from 'mongoose';
import FinancialGoal from './server/models/FinancialGoal.js';
import Savings from './server/models/Savings.js';
import Expense from './server/models/Expense.js';
import Income from './server/models/Income.js'; // Missing import for Income
import TotalSavings from './server/models/TotalSavings.js'; // Missing import for TotalSavings
import dotenv from 'dotenv';
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("✅ Connected to MongoDB"))
  .catch(err => console.error("❌ MongoDB Connection Error:", err));

// Sample Financial Goals Data
const financialGoalsData = [
  { name: 'Emergency Fund', target: 50000, current: 20000 },
  { name: 'Business Startup', target: 100000, current: 30000 }
];

// Sample Savings Data
const savingsData = [
  { month: 'January', amount: 5000 },
  { month: 'February', amount: 7000 },
  { month: 'March', amount: 6000 },
  { month: 'April', amount: 8000 },
  { month: 'May', amount: 9000 },
  { month: 'June', amount: 11000 }
];

// Sample Expenses Data
const expenseData = [
  { category: 'Food', amount: 3000 },
  { category: 'Transport', amount: 2000 },
  { category: 'Education', amount: 4000 },
  { category: 'Business', amount: 5000 },
  { category: 'Others', amount: 1000 }
];

// Sample Income Data
const incomeData = [
  { amount: 15000 }
];

// Sample Total Savings Data
const totalSavingsData = [
  { amount: 45000 }
];

// Insert Financial Goals
FinancialGoal.insertMany(financialGoalsData)
  .then(() => {
    console.log("✅ Financial Goals Seeded Successfully");
  })
  .catch((err) => {
    console.error("❌ Error Seeding Financial Goals:", err);
  });

// Insert Savings Data
Savings.insertMany(savingsData)
  .then(() => {
    console.log("✅ Savings Seeded Successfully");
  })
  .catch((err) => {
    console.error("❌ Error Seeding Savings Data:", err);
  });

// Insert Expense Data
Expense.insertMany(expenseData)
  .then(() => {
    console.log("✅ Expenses Seeded Successfully");
  })
  .catch((err) => {
    console.error("❌ Error Seeding Expenses Data:", err);
  });

// Insert Income Data
Income.insertMany(incomeData)
  .then(() => {
    console.log("✅ Income Seeded Successfully");
  })
  .catch((err) => {
    console.error("❌ Error Seeding Income Data:", err);
  });

// Insert Total Savings Data
TotalSavings.insertMany(totalSavingsData)
  .then(() => {
    console.log("✅ Total Savings Seeded Successfully");
  })
  .catch((err) => {
    console.error("❌ Error Seeding Total Savings Data:", err);
  });