import { Navigate, Outlet } from "@solidjs/router";
import { Component, JSX, Show } from "solid-js";
import { authStore } from "../store/authStore";

function isAuthorized() {
  return (authStore.user) ? true : false;
}

const Protected: Component<{ children?: JSX.Element | JSX.Element[] }> = (props) => {
  return (
    <Show when={isAuthorized()} fallback={<Navigate href="/auth/login" />}>
      {props.children || <Outlet/>}
    </Show>
  );
};

export default Protected;
