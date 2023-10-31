import { Suspense, lazy } from 'solid-js'
import { Route, Routes, Navigate } from '@solidjs/router'
import Login from './pages/Login'
import Sidebar from './components/Sidebar'
import NotFound from './pages/NotFound'
import Protected from './components/Protected'
import LoadingAnimation from './components/LoadingAnimation'

const Home = lazy(() => import('./pages/Home'));
const Timetable = lazy(() => import('./pages/Timetable'));
const Setting = lazy(() => import('./pages/Setting'));

function App() {

  return (
    <>
      <Suspense fallback={<LoadingAnimation/>}>
        <Routes>
          <Route path="/auth/login" component={Login} />
          <Route path="/*" element={<Protected><Sidebar/></Protected>}>
            <Route path="/" component={Home} />
            <Route path="/home" component={Home} />
            <Route path="/timetable" component={Timetable} />
            <Route path="/setting" component={Setting} />
          </Route>
          <Route path="/*" component={NotFound} />
        </Routes>
      </Suspense>
      {/* <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} class="logo" alt="Vite logo" />
        </a>
        <a href="https://solidjs.com" target="_blank">
          <img src={solidLogo} class="logo solid" alt="Solid logo" />
        </a>
      </div>
      <h1>Vite + Solid</h1>
      <div class="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count()}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p class="read-the-docs">
        Click on the Vite and Solid logos to learn more
      </p> */}
    </>
  )
}

export default App
