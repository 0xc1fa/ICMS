import { Component, createSignal } from "solid-js";
import { styled } from "solid-styled-components";
import { BsBodyText } from 'solid-icons/bs'
import { setAuthStore, authStore } from "../store/authStore";
import { useNavigate } from "@solidjs/router";
import { AuthStore } from "../store/authStore";
import { v4 as uuid4 } from 'uuid';
import axios from "axios";

const Auth: Component = () => {
  
  let videoRef: HTMLVideoElement | undefined;
  let stream: MediaStream | undefined;
  const navigate = useNavigate();
  const [useFaceAuth, setUseFaceAuth] = createSignal(false);

  const handleSubmit = async () => {
    setAuthStore('name', "Chan Yat Fu")
    setAuthStore('studentId', '3035690001')
    setAuthStore('email', 'chanyatfu0616@gmail.com')
    setAuthStore('sessionId', uuid4())
    const loginSessionAdd = await axios.post(
      `http://localhost:8000/add-login-session/`, {},
      {
        params: {
          student_id: authStore.studentId,
          session_id: authStore.sessionId,
        }
      }
    )
    console.log(authStore.studentId)
    console.log(authStore.sessionId)
    console.log(loginSessionAdd)
    navigate('/home')
  }

  const activateFaceAuth = async () => {
    const accessCamera = async () => {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } });
        if (videoRef) {
          videoRef.srcObject = stream;
          axios.get('http://localhost:8000/face-recognition/post')
            .then((res) => (res.data.student_id))
            .then((student_id) => {
              setAuthStore('studentId', student_id)
              console.log(student_id)
              axios.get(`http://localhost:8000/student/get/${student_id}`)
              .then((res) => (res.data.rows))
              .then(row => {
                console.log(row)
                setAuthStore('name', row.student_name)
                setAuthStore('email', row.email)
                setAuthStore('sessionId', uuid4())
                axios.post(
                  `http://localhost:8000/add-login-session/`, {},
                  {
                    params: {
                      student_id: authStore.studentId,
                      session_id: authStore.sessionId,
                    }
                  }
                )
                navigate('/home')
              })
            })
            .catch((err) => {
              console.log(err)
            })
        }
      }
    }

    try {
      accessCamera();
    } catch (err) {
      console.error("Error accessing the camera: ", err);
    }
  }

  const stopMediaStream = () => {
    if (stream) {
      const tracks = stream.getTracks();
      tracks.forEach(track => track.stop());
    }
  };

  const handleFaceAuth = async () => {
    setUseFaceAuth(!useFaceAuth())
    if (useFaceAuth()) {
      activateFaceAuth()
    } else {
      stopMediaStream()
    }
  }

  const PasswordAuth = () => (
    <>
      <InputField>
        <Label>Username</Label>
        <Input type="text" id="username" />
      </InputField>
      <InputField>
        <Label>Password</Label>
        <Input type="text" id="password" />
      </InputField>
      <ButtonField>
        <Button onClick={handleSubmit}>Log in</Button>
      </ButtonField>
    </>
  )

  const FaceAuth = styled('video')`
    background-color: #d0e1e9;
    border-radius: 0.3rem;
    margin: 1rem;
    box-sizing: border-box;
    height: fit-content;
  `

  return (
    <Container>
      <HeaderField>
        <HeadingField><Icon/><h2>HKU ICMS</h2></HeadingField>
      </HeaderField>
      {useFaceAuth() ? <FaceAuth ref={videoRef} autoplay playsinline/> : <PasswordAuth/>}
      <ButtonField>
        <HLink onClick={handleFaceAuth}>{useFaceAuth() ? "Use password" : "Use face auth"}</HLink>
      </ButtonField>
    </Container>
  )
}


const Container = styled('div')`
  display: flex;
  flex-direction: column;
  position: relative;
  width: 22rem;
  height: 35rem;
  border-radius: 0.5rem;
  background-color: #ffffff;
  box-shadow: 1rem 1rem 1rem rgba(208,225,233,255);
  justify-content: center;

  &::after {
    content: '';
    position: absolute;
    z-index: -1;
    top: 10px;
    left: -50px;
    right: -50px;
    bottom: -50px;
    border-radius: 30rem;
    background: linear-gradient(0deg, rgba(208,225,233,255) 20%, rgba(184,224,210,255));
    filter: blur(50px);
  }
`

const HeaderField = styled('div')`
  display: flex;
  margin: 0.5rem 1rem;
  align-items: start;
  gap: 0.5rem;
  border-bottom: 1px solid #d0e1e977;
  flex-direction: column;
  padding: 1rem 0;
`

const InputField = styled('div')`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin: 0.5rem 1rem;
`

const ButtonField = styled('div')`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin: 1rem;
  align-items: center;
  font-size: small;
  margin: 0.5rem 1rem;
`

const HeadingField = styled('div')`
  display: flex;
  align-items: center;
  gap: 0.75rem;
`

const Icon = styled(BsBodyText)`
  background-color: #45a08b;
  color: white;
  border-radius: 50%;
  padding: 0.375rem;
  font-size: 1.25rem;
`


const Label = styled('label')`
  color: #777777;
  font-size: small;
`

const Input = styled('input')`
  box-sizing: border-box;
  width: 100%;
  height: 2.5rem;
  border-radius: 0.3rem;
  border: 1px solid #d0e1e9;
  font-size: small;
  color: #222222;
  padding: 0 0.7rem;

  &:hover {
    border-color: #45a08b;
  }
`

const Button = styled('button')`
  box-sizing: border-box;
  width: 100%;
  height: 2.5rem;
  border-radius: 0.3rem;
  border: 1px solid #d0e1e9;
  font-size: small;
  color: white;
  background-color: #45a08b;
  padding: 0 0.7rem;
  cursor: pointer;
  transition: background-color 0.3s, color 0.1s;

  &:hover {
    background-color: white;
    color: rgba(69,160,140,255);
    border-color: rgba(69,160,140,255);
  }

  &:active {
    background-color: #e8f2ec;
    transition: background-color 0.1s;
  }
`

const HLink = styled('a')`
  color: #777777;

  &:hover {
    color: rgba(69,160,140,255) !important;
  }
`

export default Auth;
