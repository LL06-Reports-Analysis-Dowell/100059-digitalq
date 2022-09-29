import React, { useMemo } from "react";
import { useTable } from "react-table";
import { COLUMNS } from "./Colums";
import MOCK_DATA from "./MOCK_DATA.json";
import "./table.css";
import axios from "axios";

function BasicTable() {
  const baseURL = "http://100059.pythonanywhere.com/api/payload/?format=api";
  const [order, setorder] = React.useState(null);

  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setorder(response.data);
      console.log(order);
    });
  }, []);

  const columns = useMemo(() => COLUMNS, []);
  const data = useMemo(() => order, []);

  const tableInstance = useTable({
    columns,
    data,
  });
  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    tableInstance;
  return (
    <table {...getTableProps()}>
      <thead>
        {headerGroups.map((headerGroups) => (
          <tr {...headerGroups.getHeaderGroupProps()}>
            {headerGroups.headers.map((column) => (
              <th {...column.getHeaderProps()}> {column.render("Header")}</th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map((cell) => {
                return <td {...cell.getCellProps()}>{cell.render("Cell")}</td>;
              })}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default BasicTable;
