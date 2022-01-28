import React from 'react';
import Employee from './Employee';
import { Container, Table } from 'react-bootstrap';

class EmployeeList extends React.Component {
    constructor(props) {
        super(props);
        this.state = { };
    }

    getRows(csv) {
        const rows = csv.split("\n");
        let header;
        let table = [];
        rows.map(function (row, index) {
            if(index === 0) {
                header = row.split(",");
            } else {
                if(index !== rows.length-1) table.push(row.split(","))
            }
        });
        return [header, table];
    };

    render() {
        const [header, table] = this.getRows(this.props.result);
        return (
            <Container className="p-3">
            <Table striped bordered hover>
                <thead>
                    <tr>
                        { header &&
                            header.map((row, index) => {
                                return <th key={index}>{row}</th>
                            })
                        }
                    </tr>
                </thead>
                <tbody>
                    { table && 
                        table.map((row, index) => {
                            return <Employee name={row[0]} id={row[1]} O={row[2]} C={row[3]} E={row[4]} A={row[5]} N={row[6]} authority={row[7]} prob={row[8]} response={row[9]} key={index} />;
                        })
                    }
                </tbody>
            </Table>
            </Container>
        );
    }
}

export default EmployeeList;