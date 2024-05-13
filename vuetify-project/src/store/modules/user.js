import axios from "axios";
const url = "http://localhost:5000/api";

// initial state
const state = {
  currentUser: null,
  isLogin: false,
};

// getters
const getters = {};

// actions
const actions = {
  async login({ commit }, payload) {
    try {
      const res = await axios.post(`${url}/login`, payload);
      if (res.status == 200 && res.data?.success) {
        commit("setIsLogin", true);
        commit("setCurrentUser", res.data?.user);
        localStorage.setItem("isLogin", "true");
      } else {
        commit("setIsLogin", false);
        commit("setCurrentUser", null);
        localStorage.removeItem("isLogin");
      }
      return res.data;
    } catch (error) {
      console.log(error);
    }
  },
  async register({ commit }, payload) {
    try {
      const res = await axios.post(`${url}/register`, payload);
      if (res.status == 200 && res.data?.success) {
        commit("setIsLogin", true);
        commit("setCurrentUser", res.data?.user);
        localStorage.setItem("isLogin", "true");
      } else {
        commit("setIsLogin", false);
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
  setIsLogin(state, isLogin) {
    state.isLogin = isLogin;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
