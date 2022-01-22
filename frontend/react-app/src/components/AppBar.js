import { Container, Nav, Navbar } from 'react-bootstrap';

function AppBar() {
    return (
        <Navbar bg="primary" variant="dark">
            <Container>
            <Navbar.Brand href="#home">対応策計算デモ</Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link href="/">ホーム</Nav.Link>
            </Nav>
            </Container>
        </Navbar>
    );
}

export default AppBar;