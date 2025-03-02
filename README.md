# AI-Powered Financial Advisor

## Overview

The **AI-Powered Financial Advisor** is a comprehensive solution designed to cater to both tech-savvy users and individuals with limited digital proficiency, particularly in rural India. This project is divided into two major components:

- **Web Application for Tech-Savvy Users**: A financial dashboard with AI-driven chatbots for financial planning, investments, and budgeting.
- **AI-Powered Financial Advisor for Rural Users**: A WhatsApp and Telegram-based chatbot providing financial guidance, document processing, and automated financial updates.

## Problem Statement

Many individuals in India, especially in rural areas, face challenges in managing their finances due to:

- Lack of awareness of financial schemes and investment options.
- Limited access to user-friendly financial tools.
- Inefficiency in handling budgets, loans, and savings.
- Difficulty in processing financial documents.
- Delayed access to financial news and updates.

## Solution

This project leverages AI chatbots, local AI processing, and automated financial insights to provide users with the financial assistance they need.

### 1. Web Application for Tech-Savvy Users

A comprehensive platform integrating AI chatbots to assist users with:

- **Interactive Dashboard**: Provides real-time financial insights.
- **Learning Modules**: Includes video courses, quizzes, and AI-driven explanations for incorrect answers.
- **Budget Calculator**: Helps manage personal finances effectively.
- **Loan Eligibility & Savings Planner**: Assesses loan eligibility and suggests savings strategies.
- **Investment Guide**: AI chatbot support for personalized investment planning.
- **Goal-Based Planning**: Users can set financial goals and receive a tailored plan.
- **News Section**: Delivers financial news updates in the user’s preferred language every three hours.

### 2. AI-Powered Financial Advisor for Rural India

A chatbot-based financial assistant accessible through WhatsApp and Telegram, featuring:

- **Dedicated WhatsApp Bot**: Helps users with financial queries and document uploads (e.g., bank slips, loan approvals).
- **Local AI Processing (Ollama & Vector Embeddings)**: Secure and efficient document analysis without cloud dependency.
- **Automated Financial Updates**: Regular updates on financial advice, IPOs, stock recommendations, and government schemes.
- **Telegram Bot Integration**: Provides simplified document uploads and easy-to-understand financial insights.

## Features

- **Login**: User authentication is powered by MongoDB, where the password is securely encrypted for safe login.
- **Telegram Button**: A button on the bottom right corner that redirects users to the Telegram bot for analyzing and summarizing PDF files or images.
- **Data Storage**: The data in the dashboard is stored in MongoDB, ensuring a persistent and secure storage solution.
- **Learning Modules**: Users can learn specific financial topics using YouTube videos, followed by a quiz. The AI assistant helps by providing explanations for incorrect answers and can answer any questions related to the module.
- **Financial Tools**:
  - **Budget Goal Tracker**: A tool for tracking and managing personal financial goals.
  - **Loan Eligibility Calculator**: Helps users assess their eligibility for loans based on various parameters.
  - **Smart Saving Planner**: Assists users in planning their savings strategies.
  - **Smart Investment Guide**: An AI-powered tool that helps users make informed investment decisions.
- **Community & Mentorship**: A feature that allows users to connect with others, exchange ideas, and seek guidance from financial experts or mentors.
- **Goals Dashboard**: Allows users to create and track financial goals, such as saving for a car, home, or education.
- **News Section**: Fetches the latest financial news related to policies, schemes, and updates from the financial world.

## Screenshots

### Login

![image](https://github.com/user-attachments/assets/6caffe20-8fca-43ed-b7ac-40518dd0ddfd)



### Dashboard

![image](https://github.com/user-attachments/assets/9e59066f-bcd9-4004-a2ca-babd8fb80c7d)

### Learning Modules

![Learning Modules](<Screenshot 2025-02-09 193453.png>)

### Financial Literacy Model

![Financial Literacy Model](<Screenshot 2025-02-09 193515.png>)

### Video-Quiz

![Video-Quiz](<Screenshot 2025-02-09 193521.png>)

### Financial Tools

![Financial Tools](<Screenshot 2025-02-09 193629.png>)

### Budget Goal Tracker

![Budget Goal Tracker](<Screenshot 2025-02-09 193530.png>)

### Loan Eligibility Calculator

![Loan Eligibility Calculator](< Screenshot 2025-02-09 193538.png>)

### Smart Savings Planner

![Smart Savings Planner](< Screenshot 2025-02-09 193550.png>)

### Smart Investment Guide

![Smart Investment Guide](< Screenshot 2025-02-09 193558.png>)

### Community & Mentorship

![Community & Mentorship](< Screenshot 2025-02-09 193610.png>)

### Goals Dashboard

![Goals Dashboard](< Screenshot 2025-02-09 193620.png>)

### News

![News](< Screenshot 2025-02-09 193636.png>)

## Installation & Usage

To get started with the application, follow these steps:

### Install dependencies:

cd financial-advisor
npm install
npm run dev
