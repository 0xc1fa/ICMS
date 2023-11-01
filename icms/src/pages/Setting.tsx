import { Component, For } from "solid-js";
import NormalFlow from "../components/NormalFlowPage";
import { Skeleton } from "@suid/material"

const Setting: Component = () => {
  return (
    <NormalFlow>
      <h3>Setting</h3>
      <For each={[1,2,3,4,5,6,7,8,9,10]}>
        {() => <Skeleton width={700} style={{ "padding": "8px" }} />}
      </For>
    </NormalFlow>
  )
}

export default Setting;
