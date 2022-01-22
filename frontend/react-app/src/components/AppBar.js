import { Container, Nav, Navbar } from 'react-bootstrap';

function AppBar() {
    return (
        <Navbar bg="primary" variant="dark">
            <Container>
            <Navbar.Brand href="#home">Insider Signaling Game</Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link href="/">従業員一覧</Nav.Link>
            </Nav>
            </Container>
        </Navbar>
    );
}

export default AppBar;