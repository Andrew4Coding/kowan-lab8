import type {
  ActionFunctionArgs,
  LoaderFunctionArgs,
} from 'react-router';
import { CubeModule } from '~/modules/CubeModule';
import { CubeAction } from '~/modules/CubeModule/action';
import { CubeLoader } from '~/modules/CubeModule/loader';

export async function loader(args: LoaderFunctionArgs) {
  return CubeLoader(args);
}

export async function action(args: ActionFunctionArgs) {
  return CubeAction(args);
}

export default function CubePage() {
  return <CubeModule />;
}
