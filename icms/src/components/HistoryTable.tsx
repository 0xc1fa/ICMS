import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@suid/material"
import { Component, createSignal, onMount } from "solid-js"
import { For } from "solid-js"
import { styled } from "solid-styled-components";
// import rows from "../dummydata/loginHistory";
import axios from "axios";
import { authStore } from "../store/authStore" ;

type LoginHistoryTableRow = {
  student_id: string,
  session_id: string,
  login_time: string,
  login_duration: string,
}

type FormattedLogginHistoryRow = {
  loginDate: string,
  loginTime: string,
  loginDuration: string,
}

function formatDate(date: Date): string {
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, '0');
  const day = date.getDate().toString().padStart(2, '0');

  return `${year}-${month}-${day}`;
}

function formatTime(date: Date): string {
  const hours = date.getHours().toString().padStart(2, '0');
  const minutes = date.getMinutes().toString().padStart(2, '0');
  const seconds = date.getSeconds().toString().padStart(2, '0');

  return `${hours}:${minutes}:${seconds}`;
}

function secondToTimeString(seconds: number): string {
  // Calculate hours, minutes, and seconds
  // const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;

  // Format the string with leading zeros for minutes and seconds
  const formattedTime = [
      minutes.toString().padStart(2, '0'),
      remainingSeconds.toString().padStart(2, '0')
  ].join(':');

  return formattedTime;
}

const HistoryTable: Component<{ userId?: string }> = () => {

  const [rows, setRows] = createSignal<FormattedLogginHistoryRow[]>([])
  onMount(async () => {
    axios.get(`http://localhost:8000/login-history/${authStore.studentId}`)
    .then(res => res.data)
    .then(data => data.rows)
    .then(rows => {
      console.log(rows)
      rows = rows.map((row: LoginHistoryTableRow) => ({
        loginDate: formatDate(new Date(row.login_time)),
        loginTime: formatTime(new Date(row.login_time)),
        loginDuration: secondToTimeString(parseInt(row.login_duration))
      }))
      console.log(rows)
      setRows(rows);
    })
  })

  const HistoryTableHead = () => (
    <TableHead>
      <TableRow>
        <TableCell>Index</TableCell>
        <TableCell>Login Date</TableCell>
        <TableCell align="right">Login Time</TableCell>
        <TableCell align="right">Login Duration</TableCell>
      </TableRow>
    </TableHead>
  )

  const HistoryTableBody = () => (
    <TableBody>
      <For each={rows()}>{(row, index) => (
        <StyledTableRow
          sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
        >
          <TableCell component="th" scope="row">{index()}</TableCell>
          <TableCell align="left">{row.loginDate}</TableCell>
          <TableCell align="right">{row.loginTime}</TableCell>
          <TableCell align="right">{row.loginDuration}</TableCell>
        </StyledTableRow>
        )}
      </For>
    </TableBody>
  )

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <HistoryTableHead />
        <HistoryTableBody />
      </Table>
    </TableContainer>
  )

}

const StyledTableRow = styled(TableRow)`
  transition: background-color 0.2s ease-in-out;

  &:hover {
    background-color: #92c2b7;
  }
`


export default HistoryTable;
