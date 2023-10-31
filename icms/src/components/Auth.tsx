import { Component } from "solid-js";
import { styled } from "solid-styled-components";
import { BsBodyText } from 'solid-icons/bs'
import { setAuthStore } from "../store/authStore";
import { useNavigate } from "@solidjs/router";

const Auth: Component = () => {

  const navigate = useNavigate();

  const handleSubmit = () => {
    setAuthStore('user', {
      username: "test",
      userId: "test",
      email: "test",
      token: "test",
    })
    navigate('/home')
  }

  return (
    <Container>
      <HeaderField>
        <HeadingField><Icon/><h2>Oasis ICMS</h2></HeadingField>
      </HeaderField>
      <InputField>
        <Label for="username">Username</Label>
        <Input type="text" id="username" />
      </InputField>
      <InputField>
        <Label for="password">Password</Label>
        <Input type="text" id="password" />
      </InputField>
      <ButtonField>
        <Button onClick={handleSubmit}>Log in</Button>
        <HLink href="/auth/register">Forgot your password?</HLink>
        <HLink href="/auth/register">Register</HLink>
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
  background-color: rgba(69,160,140,255);
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
`

const Button = styled('button')`
  box-sizing: border-box;
  width: 100%;
  height: 2.5rem;
  border-radius: 0.3rem;
  border: 1px solid #d0e1e9;
  font-size: small;
  color: white;
  background-color: rgba(69,160,140,255);
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
