import React from 'react';
import Navbar from "./component/NavBar.js";
import Dashboard from './page/Dashboard.js';
import Profile from './page/Profile.js';
import Favorite from './page/Favorite.js';
import LogIn from './page/LogIn.js';
import SignUp from './page/SignUp.js';
import AuthProvider from './helper/Authentication.js';
import ProtectedRoute from './helper/ProtectedRoute.js';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';

export const AuthContext = React.createContext(null);

function App() {
  return (
    <div className="App-container">
      <BrowserRouter>      
        <AuthProvider> 
          <Routes>
            <Route path="/" element={
              <ProtectedRoute>
                <Navbar />
                <Dashboard />
              </ProtectedRoute> 
            }/>
            <Route path="/dashboard" element={
              <ProtectedRoute>
                <Navbar />
                <Dashboard />
              </ProtectedRoute> 
            }/>
            <Route path="/profile" element={
              <ProtectedRoute>
                <Navbar />
                <Profile />
              </ProtectedRoute> 
            }/>
            <Route path="/favorite" element={
              <ProtectedRoute>
                <Navbar />
                <Favorite />
              </ProtectedRoute> 
            }/>
            <Route path="/login" element={<LogIn />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
