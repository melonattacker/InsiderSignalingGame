function Employee(props) {
    return (
      <tr>
      <td>{props.id}</td>
      <td>{props.name}</td>
      <td>{props.action}</td>
      </tr>
    );
}

export default Employee;