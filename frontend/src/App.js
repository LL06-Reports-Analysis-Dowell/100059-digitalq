import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import FirstScreen from "./screens/FirstScreen";
import SecondScreen from "./screens/SecondScreen";
import ThirdScreen from "./screens/ThirdScreen";
import FourthScreen from "./screens/FourthScreen";

const router = createBrowserRouter([
  {
    path: "/",
    element: <FirstScreen />,
  },
  {
    path: "/SecondScreen",
    element: <SecondScreen />,
  },
  {
    path: "/ThirdScreen",
    element: <ThirdScreen />,
  },
  {
    path: "/FourthScreen",
    element: <FourthScreen />,
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
