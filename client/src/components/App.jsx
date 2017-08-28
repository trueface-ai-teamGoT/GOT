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

  onDrop2(acceptedFiles) {
        // const req = request.post('http://0.0.0.0:5000/');
        const req = request.post('http://localhost:3000/testpath');
        acceptedFiles.forEach(file => {
            req.attach(file.name, file);
        });
        req.end(console.log('req ended'));
    }

  onDrop(file) {
    let photo = new FormData();
    photo.append('photo', file[0]);
    let test = 'test'
    console.log('this is the photo', photo)
    request.post('/testpath')
      .send(photo)
      .end(function(err, resp) {
        if (err) { console.error(err); }
        return resp;
      });
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
