import { createStore } from "solid-js/store";

type User = {
  username: string;
  userId: string;
  email: string;
  token: string;
}

type AuthStore = {
  user: User | null;
}

export const [authStore, setAuthStore] = createStore<AuthStore>({
  user: null
})
