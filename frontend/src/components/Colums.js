export const COLUMNS = [
  {
    Header: "Product",
    accessor: "product",
    Cell: ({ cell: { value } }) => (
      <div>
        <img src={value} alt={value} />
      </div>
    ),
  },
  {
    Header: "code",
    accessor: "code",
  },
  {
    Header: "coupon",
    accessor: "coupon",
  },
  {
    Header: "counter",
    accessor: "counter",
  },
  {
    Header: "Queue",
    accessor: "queue",
  },
  {
    Header: "Time",
    accessor: "time",
  },
];
