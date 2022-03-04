import { Container, Nav, Navbar } from 'react-bootstrap';

function AppBar() {
    return (
        <Navbar bg="primary" variant="dark">
            <Container>
                <Navbar.Brand href="#home">対応策計算デモ</Navbar.Brand>
            </Container>
        </Navbar>
    );
}

export default AppBar;