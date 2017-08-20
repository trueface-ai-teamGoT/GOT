import React from 'react';
import ImagesUploader from 'react-images-uploader';
// import 'react-images-uploader/styles.css';
// import 'react-images-uploader/font.css';

class ImageUpload extends React.Component {

  render () {
    return (
      <div>
        <h2> Which Game of Thrones Character are you? </h2>
        <ImagesUploader
          url="http://localhost:3000/testpath"
          optimisticPreviews
          multiple={false}
          onLoadEnd={(err) => {
              if (err) {
                  console.error(err);
              }
          }}
          label="Upload a picture"
        />

        <p> upload your image and find out! </p>
      </div>
    )
  }
}

export default ImageUpload



