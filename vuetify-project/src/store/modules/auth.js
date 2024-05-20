import axios from "axios";
const url = "http://localhost:5000";

// initial state
const state = {
  currentUser: null,
};

// getters
const getters = {};

// actions
const actions = {
  async getUser({}, payload) {
    try {
      const res = await axios.get(`${url}/users`, {
        headers: {
          Authorization: payload?.token,
        },
      });
      return res?.data;
    } catch (error) {
      return error?.response?.data;
    }
  },
  async login({ commit }, payload) {
    try {
      const res = await axios.post(`${url}/auth/login`, payload);
      commit("setCurrentUser", res.data?.user);
      localStorage.setItem("isLoggedIn", "true");
      localStorage.setItem("email", res.data?.user?.email);
      localStorage.setItem("token", res.data?.user?.token);
      return res.data;
    } catch (error) {
      console.error(error.response.data);
      commit("setCurrentUser", null);
      localStorage.removeItem("isLoggedIn");
      localStorage.removeItem("email");
      localStorage.removeItem("token");
      return error?.response?.data;
    }
  },
  async signup({ commit }, payload) {
    try {
      const res = await axios.post(`${url}/auth/signup`, payload);
      if (res.status == 201 && res.data?.success) {
        commit("setCurrentUser", res.data?.user);
        localStorage.setItem("isLoggedIn", "true");
      } else {
        commit("setCurrentUser", null);
        localStorage.removeItem("isLoggedIn");
      }
      return res.data;
    } catch (error) {
      console.log(error);
    }
  },
};

// mutations
const mutations = {
  setCurrentUser(state, user) {
    state.currentUser = user;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
