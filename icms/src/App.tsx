import { Suspense, lazy, onCleanup, onMount } from 'solid-js'
import { Route, Routes } from '@solidjs/router'
import Login from './pages/Login'
import Sidebar from './components/Sidebar'
import NotFound from './pages/NotFound'
import Protected from './components/Protected'
import LoadingAnimation from './components/LoadingAnimation'
import Home from './pages/Home'
import History from './pages/History'
import Setting from './pages/Setting'
import { authStore } from "./store/authStore";
import axios from 'axios';


function App() {
  let intervalId: number;

  onMount(async () => {
    intervalId = setInterval(fetchData, 1000);
  });

  const fetchData = async () => {
    if (authStore.sessionId === null) return;
    const response = await axios.put('http://localhost:8000/update-login-session/', {}, {
      params: {
        session_id: authStore.sessionId
      }
    })
    console.log(response);
    // try {
    //   const response = await fetch(`http://localhost:8000/update-login-session/`);
    //   const data = await response.json();
    //   console.log(data);
    // } catch (error) {
    //   console.error('Error fetching data:', error);
    // }
  };

  onCleanup(() => {
    clearInterval(intervalId);
  });

  return (
    <>
      <Suspense fallback={<LoadingAnimation/>}>
        <Routes>
          <Route path="/auth/login" component={Login} />
          <Route path="/*" element={<Protected><Sidebar/></Protected>}>
            <Route path="/" component={Home} />
            <Route path="/home" component={Home} />
            <Route path="/history" component={History} />
            <Route path="/setting" component={Setting} />
          </Route>
          <Route path="/*" component={NotFound} />
        </Routes>
      </Suspense>
    </>
  )
}

export default App
