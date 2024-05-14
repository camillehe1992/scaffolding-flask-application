import axios from "axios";
const url = "http://localhost:5000/api";

// initial state
const state = {
  currentUser: null,
};

// getters
const getters = {};

// actions
const actions = {
  async login({ commit }, payload) {
    try {
      const res = await axios.post(`${url}/login`, payload);
      console.log(res);
      if (res.status == 201 && res.data?.success) {
        commit("setCurrentUser", res.data?.user);
        localStorage.setItem("isLogin", "true");
        localStorage.setItem("token", res.data?.user?.token);
      } else {
        commit("setCurrentUser", null);
        localStorage.removeItem("isLogin");
        localStorage.removeItem("token");
      }
      return res.data;
    } catch (error) {
      console.log(error);
    }
  },
  async signup({ commit }, payload) {
    try {
      const res = await axios.post(`${url}/signup`, payload);
      if (res.status == 201 && res.data?.success) {
        commit("setCurrentUser", res.data?.user);
        localStorage.setItem("isLogin", "true");
      } else {
        commit("setCurrentUser", null);
        localStorage.removeItem("isLogin");
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
