import type {
  ActionFunctionArgs,
  LoaderFunctionArgs,
} from 'react-router';
import { CircleModule } from '~/modules/CircleModule';
import { CircleAction } from '~/modules/CircleModule/action';
import { CircleLoader } from '~/modules/CircleModule/loader';

export async function loader(args: LoaderFunctionArgs) {
  return CircleLoader(args);
}

export async function action(args: ActionFunctionArgs) {
  return CircleAction(args);
}

export default function CirclePage() {
  return <CircleModule />;
}
