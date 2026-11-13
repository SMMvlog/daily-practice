import { useState } from "react";
import axios from "axios";
import "./index.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  const [loginData, setLoginData] = useState({
    user_id: "",
    email_id: "",
  });

  const [users, setUsers] = useState([]);
  const [searchName, setSearchName] = useState("");

  const [userData, setUserData] = useState({
    name: "",
    email_id: "",
    is_active: true,
    location: "",
  });

  const [orderData, setOrderData] = useState({
    product_name: "",
    quantity: 1,
    user_id: "",
  });

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  // -----------------------------
  // LOGIN
  // -----------------------------

  const login = async (e) => {
    e.preventDefault();

    try {
      setError("");
      setMessage("");

      const response = await axios.post(
        `${API_URL}/login`,
        loginData
      );

      const jwtToken = response.data.token;

      localStorage.setItem("token", jwtToken);
      setToken(jwtToken);

      setMessage("Login successful");

    } catch (err) {
      console.log(err);

      setError(
        err.response?.data?.detail || "Login failed"
      );
    }
  };

  // -----------------------------
  // LOGOUT
  // -----------------------------

  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);
    setUsers([]);
  };

  // -----------------------------
  // GET USERS
  // -----------------------------

  const getUsers = async () => {
    try {
      setError("");

      const response = await axios.get(
        `${API_URL}/get_users/name`,
        {
          params: searchName
            ? { name: searchName }
            : {},
          headers: {
            Authorization: token,
          },
        }
      );

      setUsers(response.data);

    } catch (err) {
      console.log(err);

      setError(
        err.response?.data?.detail || "Unable to get users"
      );
    }
  };

  // -----------------------------
  // ADD USER
  // -----------------------------

  const addUser = async (e) => {
    e.preventDefault();

    try {
      setError("");

    const response = await axios.post(
  `${API_URL}/add_user`,
  userData,
  {
    headers: {
      Authorization: `${token}`,
    },
  }
);

      setMessage(
        `User ${response.data.name} created successfully`
      );

      setUserData({
        name: "",
        email_id: "",
        is_active: true,
        location: "",
      });

    } catch (err) {
      console.log(err);

      setError(
        err.response?.data?.detail || "Unable to create user"
      );
    }
  };

  // -----------------------------
  // CREATE ORDER
  // -----------------------------

  const createOrder = async (e) => {
  e.preventDefault();

  try {
    setError("");
    setMessage("");

    const response = await axios.post(
      `${API_URL}/create_order`,
      {
        product_name: orderData.product_name,
        quantity: Number(orderData.quantity),
        user_id: Number(orderData.user_id),
      },
      {
        headers: {
          Authorization: `${token}`,
        },
      }
    );

    setMessage("Order created successfully");

    setOrderData({
      product_name: "",
      quantity: 1,
      user_id: "",
    });

  } catch (err) {
    console.log(err);

    setError(
      err.response?.data?.detail ||
      "Unable to create order"
    );
  }
};

  // -----------------------------
  // LOGIN PAGE
  // -----------------------------

  if (!token) {
    return (
      <div className="login-container">

        <div className="login-card">

          <h1>FastAPI App</h1>

          <p className="subtitle">
            Login to continue
          </p>

          <form onSubmit={login}>

            <label>User ID</label>

            <input
              type="number"
              placeholder="Enter user ID"
              value={loginData.user_id}
              onChange={(e) =>
                setLoginData({
                  ...loginData,
                  user_id: e.target.value,
                })
              }
              required
            />

            <label>Email</label>

            <input
              type="email"
              placeholder="example@gmail.com"
              value={loginData.email_id}
              onChange={(e) =>
                setLoginData({
                  ...loginData,
                  email_id: e.target.value,
                })
              }
              required
            />

            <button type="submit">
              Login
            </button>

          </form>

          {message && (
            <div className="success">
              {message}
            </div>
          )}

          {error && (
            <div className="error">
              {error}
            </div>
          )}

        </div>

      </div>
    );
  }

  // -----------------------------
  // DASHBOARD
  // -----------------------------

  return (
    <div className="app">

      {/* NAVBAR */}

      <nav className="navbar">

        <div className="logo">
          FastAPI Dashboard
        </div>

        <button
          className="logout-button"
          onClick={logout}
        >
          Logout
        </button>

      </nav>

      <div className="container">

        <h1>Dashboard</h1>

        {message && (
          <div className="success">
            {message}
          </div>
        )}

        {error && (
          <div className="error">
            {error}
          </div>
        )}

        {/* USERS */}

        <section className="card">

          <div className="card-header">

            <h2>Users</h2>

            <button onClick={getUsers}>
              Load Users
            </button>

          </div>

          <div className="search-box">

            <input
              type="text"
              placeholder="Search user by name"
              value={searchName}
              onChange={(e) =>
                setSearchName(e.target.value)
              }
            />

            <button onClick={getUsers}>
              Search
            </button>

          </div>

          {users.length > 0 && (

            <table>

              <thead>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Location</th>
                  <th>Active</th>
                </tr>
              </thead>

              <tbody>

                {users.map((user, index) => (

                  <tr key={index}>

                    <td>{user.name}</td>

                    <td>{user.email_id}</td>

                    <td>
                      {user.location || "-"}
                    </td>

                    <td>
                      {user.is_active
                        ? "Yes"
                        : "No"}
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          )}

        </section>


        {/* ADD USER */}

        <section className="card">

          <h2>Add User</h2>

          <form onSubmit={addUser}>

            <div className="form-row">

              <div>
                <label>Name</label>

                <input
                  type="text"
                  placeholder="User name"
                  value={userData.name}
                  onChange={(e) =>
                    setUserData({
                      ...userData,
                      name: e.target.value,
                    })
                  }
                  required
                />
              </div>

              <div>
                <label>Email</label>

                <input
                  type="email"
                  placeholder="user@gmail.com"
                  value={userData.email_id}
                  onChange={(e) =>
                    setUserData({
                      ...userData,
                      email_id: e.target.value,
                    })
                  }
                  required
                />
              </div>

            </div>


            <div className="form-row">

              <div>

                <label>Location</label>

                <input
                  type="text"
                  placeholder="Mumbai"
                  value={userData.location}
                  onChange={(e) =>
                    setUserData({
                      ...userData,
                      location: e.target.value,
                    })
                  }
                />

              </div>

              <div className="checkbox">

                <label>
                  <input
                    type="checkbox"
                    checked={userData.is_active}
                    onChange={(e) =>
                      setUserData({
                        ...userData,
                        is_active:
                          e.target.checked,
                      })
                    }
                  />

                  Active User
                </label>

              </div>

            </div>

            <button type="submit">
              Add User
            </button>

          </form>

        </section>


        {/* CREATE ORDER */}

        <section className="card">

          <h2>Create Order</h2>

          <form onSubmit={createOrder}>

            <div className="form-row">

              <div>

                <label>Product Name</label>

                <input
                  type="text"
                  placeholder="Laptop"
                  value={orderData.product_name}
                  onChange={(e) =>
                    setOrderData({
                      ...orderData,
                      product_name:
                        e.target.value,
                    })
                  }
                  required
                />

              </div>


              <div>

                <label>Quantity</label>

                <input
                  type="number"
                  min="1"
                  value={orderData.quantity}
                  onChange={(e) =>
                    setOrderData({
                      ...orderData,
                      quantity:
                        e.target.value,
                    })
                  }
                  required
                />

              </div>


              <div>

                <label>User ID</label>

                <input
                  type="number"
                  placeholder="1"
                  value={orderData.user_id}
                  onChange={(e) =>
                    setOrderData({
                      ...orderData,
                      user_id:
                        e.target.value,
                    })
                  }
                  required
                />

              </div>

            </div>

            <button type="submit">
              Create Order
            </button>

          </form>

        </section>

      </div>

    </div>
  );
}

export default App;