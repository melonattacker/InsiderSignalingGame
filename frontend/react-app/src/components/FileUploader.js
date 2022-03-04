import React from 'react';
import { Button } from 'react-bootstrap';

class FileUploader extends React.Component {
    constructor(props) {
        super(props);
        this.state = { result: "" };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.fileInput = React.createRef();
    }

    handleSubmit(event) {
        event.preventDefault();
        if(this.fileInput.current.files.length === 0) return;
        const data = new FormData();
        data.append('file', this.fileInput.current.files[0]);
        fetch('http://localhost:8080/', {
            method: 'POST',
            body: data
        })
        .then(res => res.blob())
        .then(async(blob) => {
            const result = await blob.text();
            this.props.onChangeResult(result);
        })
        .catch(err => {
            console.log(err);
        });
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input type='file' accept='.csv' ref={this.fileInput} />
                <Button type="submit" variant="outline-primary">送信</Button>
            </form>
        );
    }
}

export default FileUploader;