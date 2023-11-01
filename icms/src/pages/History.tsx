import { Component } from "solid-js";
import HistoryTable from "../components/HistoryTable";
import NormalFlow from "../components/NormalFlowPage";

const History: Component = () => {
  return (
    <NormalFlow>
      <h3>History</h3>
      <HistoryTable/>
    </NormalFlow>
  )
}

export default History;
