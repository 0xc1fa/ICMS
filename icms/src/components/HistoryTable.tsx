import { 
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@suid/material"
import { Component } from "solid-js"
import { For } from "solid-js"
import { styled } from "solid-styled-components";
import rows from "../dummydata/loginHistory";

const HistoryTable: Component<{ userId?: string }> = () => {

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
      <For each={rows}>{(row, index) => (
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
