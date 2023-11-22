import { createStore } from "solid-js/store";

export type AuthStore = {
  sessionId: string | null;
  name: string | null;
  studentId: string | null;
  email: string | null;
}

export const [authStore, setAuthStore] = createStore<AuthStore>({
  name: null,
  studentId: null,
  email: null,
  sessionId: null
})
