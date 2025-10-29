import type {
  ActionFunctionArgs,
  LoaderFunctionArgs,
} from 'react-router';
import { SquareModule } from '~/modules/SquareModule';
import { SquareAction } from '~/modules/SquareModule/action';
import { SquareLoader } from '~/modules/SquareModule/loader';

export async function loader(args: LoaderFunctionArgs) {
  return SquareLoader(args);
}

export async function action(args: ActionFunctionArgs) {
  return SquareAction(args);
}

export default function SquarePage() {
  return <SquareModule />;
}
