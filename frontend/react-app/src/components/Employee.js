function Employee(props) {
    return (
      <tr>
      <td>{props.name}</td>
      <td>{props.id}</td>
      <td>{props.O}</td>
      <td>{props.C}</td>
      <td>{props.E}</td>
      <td>{props.A}</td>
      <td>{props.N}</td>
      <td>{props.authority}</td>
      <td>{props.prob}</td>
      <td>{props.response}</td>
      </tr>
    );
}

export default Employee;