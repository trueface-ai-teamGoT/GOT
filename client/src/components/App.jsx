// import React from 'react'
// import ImageUpload from './ImageUpload.jsx'

// class App extends React.Component {

//   render () {
//     return (
//       <ImageUpload></ImageUpload>
//     )
//   }
// }

// export default App

import React,{Component} from 'react';
import Dropzone from 'react-dropzone';
import request from 'superagent';




class App extends React.Component {
  constructor() {
    super()
    this.state = { files: [] }
  }

  onDrop(acceptedFiles) {
        const req = request.post('http://0.0.0.0:5000/');
        acceptedFiles.forEach(file => {
            req.attach(file.name, file);
        });
        req.end(console.log('req ended'));
    }

  render() {
    return (
      <section>
        <div className="dropzone">
          <Dropzone onDrop={this.onDrop.bind(this)}>
            <p>Try dropping some files here, or click to select files to upload.</p>
          </Dropzone>
        </div>
        <aside>
          <h2>Dropped files</h2>
          <ul>
            {
              this.state.files.map(f => <li>{f.name} - {f.size} bytes</li>)
            }
          </ul>
        </aside>
      </section>
    );
  }
}

export default App
