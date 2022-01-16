import React from 'react';
import Employee from './Employee';
import { Container, Table } from 'react-bootstrap';

class EmployeeList extends React.Component {
    constructor(props) {
        super(props);
        this.state = { employees: []};
    }

    async componentDidMount() {
        const response = await fetch("http://localhost:8080/employee");
        const data = await response.json();
        await this.setState({ employees: data })
    }

    render() {
        return (
            <Container className="p-3">
            <Table striped bordered hover>
                <thead>
                    <tr>
                    <th>ID</th>
                    <th>名前</th>
                    <th>対応策</th>
                    </tr>
                </thead>
                <tbody>
                    { this.state.employees && 
                        this.state.employees.map((row, index) => {
                            return <Employee id={row[0]} name={row[1]} action={row[2]} key={index} />;
                        })
                    }
                </tbody>
            </Table>
            </Container>
        );
    }
}

export default EmployeeList;