import { reactive, toRefs, watch } from "vue";
import { useApi } from "./api";

const AUTH_KEY = "token";
const AUTH_TOKEN = "access_token";

const state = reactive({
  authenticating: false,
  user: undefined,
  error: undefined,
});

// Read access token from local storage
const token = window.localStorage.getItem(AUTH_KEY);

if (token) {
  const { loading, error, data, get } = useApi("/auth/user");
  state.authenticating = true;

  get({}, { headers: { Authorization: `Bearer ${token}` } });

  watch([loading], () => {
    if (error.value) {
      window.localStorage.removeItem(AUTH_KEY);
    } else if (data.value) {
      state.user = data.value;
    }

    state.authenticating = false;
  });
}

export const useAuth = () => {
  const setUser = (payload, remember) => {
    if (remember) {
      // Save
      window.localStorage.setItem(AUTH_KEY, payload[AUTH_TOKEN]);
    }

    state.user = payload;
    state.error = undefined;
  };

  const logout = () => {
    window.localStorage.removeItem(AUTH_KEY);
    return Promise.resolve((state.user = undefined));
  };

  return {
    setUser,
    logout,
    ...toRefs(state), // authenticating, user, error
  };
};
