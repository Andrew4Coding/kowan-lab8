import type {
  ActionFunctionArgs,
  LoaderFunctionArgs,
} from 'react-router';
import { TubeModule } from '~/modules/TubeModule';
import { TubeAction } from '~/modules/TubeModule/action';
import { TubeLoader } from '~/modules/TubeModule/loader';

export async function loader(args: LoaderFunctionArgs) {
  return TubeLoader(args);
}

export async function action(args: ActionFunctionArgs) {
  return TubeAction(args);
}

export default function TubePage() {
  return <TubeModule />;
}
